#!/usr/bin/python3
import numpy as np
from scipy.spatial.transform import Rotation as R
from spatialmath import SE3
import roboticstoolbox as rtb
from roboticstoolbox import RevoluteMDH
import time

class RobotKinematics:
    def __init__(self):
        # Joint limits
        self.q_min = np.array([-np.pi, -np.pi, -np.pi])
        self.q_max = np.array([ np.pi,  np.pi,  np.pi])
        
        # Workspace bounds
        self.x_min, self.x_max = -0.529921, 0.529921
        self.y_min, self.y_max = -0.529200, 0.530097
        self.z_min, self.z_max = -0.299425, 0.759486
        
        # URDF Joint Parameters (for accurate FK)
        self.j1_xyz = np.array([0, 0, 0.23])
        self.j1_rpy = np.array([0, 0, 0])
        self.j2_xyz = np.array([0, -0.12, 0])
        self.j2_rpy = np.array([-np.pi/2, -np.pi/2, 0])
        self.j3_xyz = np.array([0.25, 0, 0.1])
        self.j3_rpy = np.array([0, 0, 0])
        self.ee_xyz = np.array([0.28, 0, 0])
        self.ee_rpy = np.array([0, 0, 0])
        
        # Robotics Toolbox model (matches URDF!)
        self.robot = rtb.DHRobot([
            RevoluteMDH(d=0.23,  alpha=0,       a=0,    offset=0),
            RevoluteMDH(d=-0.12, alpha=-np.pi/2, a=0,   offset=-np.pi/2),
            RevoluteMDH(d=0.1,   alpha=0,       a=0.25, offset=0),
        ], tool=SE3.Tx(0.28), name="3R_Robot")
    
    # ---------------- FK -----------------
    
    def rpy_to_matrix(self, rpy):
        return R.from_euler('xyz', rpy).as_matrix()
    
    def rotation_z(self, theta):
        c, s = np.cos(theta), np.sin(theta)
        return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    
    def create_transform(self, xyz, rpy, q=0):
        R_fixed = self.rpy_to_matrix(rpy)
        R_joint = self.rotation_z(q)
        R_total = R_fixed @ R_joint
        T = np.eye(4)
        T[:3, :3] = R_total
        T[:3, 3] = xyz
        return T
    
    def forward_kinematics(self, q):
        """URDF-based FK (ground truth)"""
        T = np.eye(4)
        T = T @ self.create_transform(self.j1_xyz, self.j1_rpy, q[0])
        T = T @ self.create_transform(self.j2_xyz, self.j2_rpy, q[1])
        T = T @ self.create_transform(self.j3_xyz, self.j3_rpy, q[2])
        T_ee = np.eye(4)
        T_ee[:3, :3] = self.rpy_to_matrix(self.ee_rpy)
        T_ee[:3, 3] = self.ee_xyz
        T = T @ T_ee
        return T
    
    def get_position(self, q):
        T = self.forward_kinematics(q)
        return T[:3, 3]
    
    def get_rotation(self, q):
        T = self.forward_kinematics(q)
        return T[:3, :3]
    
    def get_pose(self, q):
        T = self.forward_kinematics(q)
        return T[:3, 3], T[:3, :3]
    
    
    # ---------------- Jacobians -----------------
    
    def jacobian_world(self, q, epsilon=1e-6):
        J = np.zeros((3, 3))
        pos_0 = self.get_position(q)
        for i in range(3):
            dq = q.copy()
            dq[i] += epsilon
            pos_pert = self.get_position(dq)
            J[:, i] = (pos_pert - pos_0) / epsilon
        return J
    
    def jacobian_ee(self, q):
        J_w = self.jacobian_world(q)
        R_we = self.get_rotation(q)
        return R_we.T @ J_w
    
    # ---------------- Velocity Mapping -----------------
    
    def ee_velocity_to_qdot(self, q, v, frame='world'):
        if frame == 'world':
            J = self.jacobian_world(q)
        elif frame == 'ee':
            J = self.jacobian_ee(q)
        else:
            raise ValueError("frame must be 'world' or 'ee'")
        return np.linalg.pinv(J) @ v
    
    # ---------------- Singularity detection -----------------

    def singularity_measure(self, q):
        U, S, Vt = np.linalg.svd(self.jacobian_world(q))
        return S[-1]   # smallest singular value

    def is_near_singularity(self, q, threshold=0.01):
        return self.singularity_measure(q) < threshold
    
    # ---------------- IK ------------------------------------
    
    def inverse_kinematics(self, target_pos, q_init=None, max_time=0.5):
        start_time = time.time()

        # Workspace check
        if not self.is_in_workspace(target_pos, tolerance=0.05):
            print(f"DEBUG: Target {target_pos} is outside workspace!")
            print(f"  Workspace X: [{self.x_min}, {self.x_max}]")
            print(f"  Workspace Y: [{self.y_min}, {self.y_max}]")
            print(f"  Workspace Z: [{self.z_min}, {self.z_max}]")
            return None

        T_target = SE3(target_pos[0], target_pos[1], target_pos[2])

        initial_guesses = [
            [0.0, 0.0, 0.0],
            [0.0, np.pi/4, 0.0],
            [0.0, -np.pi/4, 0.0],
            [np.pi/4, 0.0, 0.0],
            [-np.pi/4, 0.0, 0.0],
            [0.0, np.pi/2, -np.pi/4],
            [0.0, -np.pi/2, np.pi/4],
            [np.pi/2, 0.0, 0.0],
            [-np.pi/2, 0.0, 0.0],
            [np.pi/3, np.pi/6, np.pi/6],
        ]

        if q_init is not None:
            initial_guesses.insert(0, q_init[:3] if len(q_init) > 3 else q_init)

        best_solution = None
        best_error = float('inf')

        for q0 in initial_guesses:
            # Hard time check
            if time.time() - start_time > max_time:
                print(f"DEBUG: IK timeout after {max_time:.2f}s, best error {best_error:.4f}")
                break

            try:
                sol = self.robot.ikine_LM(
                    T_target,
                    q0=q0,
                    mask=[1, 1, 1, 0, 0, 0],
                    ilimit=60  # <=== lower iteration limit
                )

                if sol.success:
                    q = np.array(sol.q)

                    # joint limits
                    if not all(self.q_min[i] <= q[i] <= self.q_max[i] for i in range(3)):
                        continue

                    pos_check = self.get_position(q)
                    error = np.linalg.norm(pos_check - np.array(target_pos))

                    if error < best_error:
                        best_error = error
                        best_solution = q

                        if error < 0.02:  # 2 cm
                            return best_solution

            except Exception as e:
                print(f"IK error with q0={q0}: {e}")
                continue

        if best_solution is not None and best_error < 0.1:
            print(f"DEBUG: Found solution with error {best_error:.4f}m (timeout-safe)")
            return best_solution

        print(f"DEBUG: No solution found within time. Best error was {best_error:.4f}m")
        return None
    
    # ---------------- Workspace ----------------------------
    
    def is_in_workspace(self, point, tolerance=0.01):
        x, y, z = point
        return (self.x_min - tolerance <= x <= self.x_max + tolerance and
                self.y_min - tolerance <= y <= self.y_max + tolerance and
                self.z_min - tolerance <= z <= self.z_max + tolerance)
    
    def calculate_workspace_bounds(self, n_samples_per_joint=50):
        print(f'Calculating workspace with {n_samples_per_joint}^3 samples...')
        q1_range = np.linspace(self.q_min[0], self.q_max[0], n_samples_per_joint)
        q2_range = np.linspace(self.q_min[1], self.q_max[1], n_samples_per_joint)
        q3_range = np.linspace(self.q_min[2], self.q_max[2], n_samples_per_joint)
        
        positions = []
        for q1 in q1_range:
            for q2 in q2_range:
                for q3 in q3_range:
                    pos = self.get_position(np.array([q1, q2, q3]))
                    positions.append(pos)
        
        positions = np.array(positions)
        self.x_min, self.x_max = positions[:, 0].min(), positions[:, 0].max()
        self.y_min, self.y_max = positions[:, 1].min(), positions[:, 1].max()
        self.z_min, self.z_max = positions[:, 2].min(), positions[:, 2].max()
        
        print('='*60)
        print('WORKSPACE BOUNDS:')
        print(f"  X: [{self.x_min:.6f}, {self.x_max:.6f}] m")
        print(f"  Y: [{self.y_min:.6f}, {self.y_max:.6f}] m")
        print(f"  Z: [{self.z_min:.6f}, {self.z_max:.6f}] m")
        print('='*60)
        return positions


if __name__ == '__main__':
    print("="*60)
    print("Robot Kinematics - URDF FK + RTB IK")
    print("="*60)
    
    robot = RobotKinematics()
    
    # # Test FK
    # q_test = np.array([0.0, 0.0, 0.0])
    # pos = robot.get_position(q_test)
    # print(f"\nFK at [0,0,0]: [{pos[0]:.6f}, {pos[1]:.6f}, {pos[2]:.6f}]")
    
    # # Test IK
    # target = [0.3, 0.0, 0.5]
    # print(f"\nTesting IK for target: {target}")
    # solution = robot.inverse_kinematics(target)
    # if solution is not None:
    #     print(f"✓ Solution: {solution}")
    #     pos_check = robot.get_position(solution)
    #     print(f"  Verification: [{pos_check[0]:.6f}, {pos_check[1]:.6f}, {pos_check[2]:.6f}]")
    #     error = np.linalg.norm(pos_check - np.array(target))
    #     print(f"  Error: {error*1000:.2f} mm")
    # else:
    #     print("✗ No solution found")
    # # Test at home position [0,0,0]
    # q = [0.0, 0.0, 0.0]
    # pos, R = robot.get_pose(q)

    # print(f"Position: {pos}")
    # print(f"Expected: [0.000, -0.020, 0.760]")
    for q in [
        np.array([0.0, 0.0, 0.0]),
        np.array([0.5, -0.7, 0.3]),
        np.array([1.0, -1.0, 0.5]),
    ]:
        sigma_min = robot.singularity_measure(q)
        pos = robot.get_position(q)
        print(f"q = {q},  pos = {pos},  sigma_min = {sigma_min:.6e}")