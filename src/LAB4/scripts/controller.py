#!/usr/bin/python3
import rclpy
from rclpy.node import Node
import numpy as np
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import String
from robot_interfaces.srv import ModeSelect, InverseKinematic, RandomEndEffector
from LAB4.workspace_analysis import RobotKinematics


class controller(Node):
    """
    Main robot controller supporting 4 modes:
    - IDLE: No movement
    - IPK: Inverse Position Kinematics (move to target)
    - TO: Teleoperation (manual control)
    - AM: Auto Mode (continuous random targets)
    """
    
    FRAME_WORLD = 1.0
    FRAME_EE = -1.0
    RESET_CMD = -999.0
    
    def __init__(self):
        super().__init__('controller')
        self.kinematics = RobotKinematics()
        
        self.mode = "IDLE"
        self.teleop_frame = "world"
        
        # Joint positions (start at safe config to avoid singularity)
        self.safe_q = np.array([0.5, -0.7, 0.3])
        self.current_q = self.safe_q.copy()
        self.target_q = np.zeros(3)
        
        # Motion state
        self.is_moving = False
        self.joint_velocities = np.zeros(3)
        
        # Auto mode state
        self.am_waiting = False
        self.am_future = None
        
        # Client
        self.random_pose_client = self.create_client(RandomEndEffector, 'random_pose')

        # Subscribers
        self.target_sub = self.create_subscription(PoseStamped, 'target', self.target_callback, 10)
        self.cmd_vel_sub = self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)
       
        # Publishers
        self.joint_pub = self.create_publisher(JointState, 'joint_states', 10)
        self.status_pub = self.create_publisher(String, 'controller_status', 10)
        
        # Services
        self.create_service(ModeSelect, 'mode_select', self.mode_select_callback)
        self.create_service(InverseKinematic, 'inverse_kinematic', self.ik_service_callback)
        
        # Timer for motion control (50 Hz)
        self.motion_timer = self.create_timer(0.02, self.motion_update)
        
        # Publish initial position
        self.publish_joint_state()
        
        # Startup info
        sigma = self.kinematics.singularity_measure(self.current_q)
        self.get_logger().info('='*60)
        self.get_logger().info('Robot Controller initialized')
        self.get_logger().info(f'Mode: {self.mode}')
        self.get_logger().info(f'Initial q: {self.current_q}')
        self.get_logger().info(f'Singularity measure: {sigma:.6e}')
        self.get_logger().info('Services: /mode_select, /inverse_kinematic')
        self.get_logger().info('='*60)

  
    
    def motion_update(self):
        if self.mode == "IPK":
            self._update_ipk_motion()
        elif self.mode == "TO":
            self._update_to_motion()
        elif self.mode == "AM":
            self._update_am_motion()
        else:
            self._update_idle_motion()
    
    def _update_idle_motion(self):
        self.publish_joint_state()
    
    def _update_ipk_motion(self):
        if not self.is_moving:
            return
        
        step_size = 0.05
        error = self.target_q - self.current_q
        max_error = np.max(np.abs(error))
        
        if max_error < 0.001:
            self.current_q = self.target_q.copy()
            self.is_moving = False
            self.get_logger().info('✓ Reached target')
        else:
            self.current_q += error * step_size
        
        pos = self.kinematics.get_position(self.current_q)
        if pos[2] < 0.02:  # Floor limit check
            self.get_logger().warn("Floor limit reached. Cannot move below the floor.")
            self.is_moving = False  # Stop motion
        self.publish_joint_state()
    
    def _update_to_motion(self):
        dt = 0.02
        new_q = self.current_q + self.joint_velocities * dt
        new_q = np.clip(new_q, self.kinematics.q_min, self.kinematics.q_max)
        
        new_pos = self.kinematics.get_position(new_q)
        if self.kinematics.is_in_workspace(new_pos, tolerance=0.05):
            self.current_q = new_q
        else:
            self.get_logger().warn('⚠️ Workspace limit reached')
            self.joint_velocities = np.zeros(3)
        
        pos = self.kinematics.get_position(self.current_q)
        if pos[2] < 0.02:
            self.get_logger().warn("Floor limit reached. Cannot move below the floor.")
            self.is_moving = False  # Stop motion
        self.publish_joint_state()
    
    def _update_am_motion(self):
        
        if not self.is_moving and not self.am_waiting:
            if not self.random_pose_client.wait_for_service(timeout_sec=1.0):
                self.get_logger().warn("AM: random_pose service not available")
                return
            
            self.get_logger().info("AM: Requesting new random pose...")
            req = RandomEndEffector.Request()
            self.am_future = self.random_pose_client.call_async(req)
            self.am_waiting = True
            return

        if self.am_waiting:
            if self.am_future.done():
                self.am_waiting = False
                resp = self.am_future.result()
                
                if not resp.success:
                    self.get_logger().warn("AM: random pose request failed")
                    return
                
                target_pos = [resp.position.x, resp.position.y, resp.position.z]
                self.get_logger().info(
                    f"AM: New target → [{target_pos[0]:.3f}, {target_pos[1]:.3f}, {target_pos[2]:.3f}]"
                )
                
                solution = self.kinematics.inverse_kinematics(target_pos, self.current_q)
                if solution is None:
                    self.get_logger().warn("AM: IK failed for target")
                    return
                
                self.move_to_position(solution)
            return
        
        step_size = 0.05
        error = self.target_q - self.current_q
        if np.max(np.abs(error)) < 0.001:
            self.current_q = self.target_q.copy()
            self.is_moving = False
        else:
            self.current_q += step_size * error
        
        self.publish_joint_state()

    
    def cmd_vel_callback(self, msg):
        if msg.angular.x == self.RESET_CMD:
            self.reset_position()
            return
        
        if self.mode != "TO":
            return

        pos = self.kinematics.get_position(self.current_q)

        if pos[2] < 0.02 and msg.linear.z < 0.0:
            self.get_logger().warn("Floor limit reached. Cannot move below the floor.")
            self.joint_velocities = np.zeros(3)
            return


        if msg.angular.y == self.FRAME_WORLD:
            self.teleop_frame = "world"
            self.get_logger().info("TO Frame → WORLD")
            return
        if msg.angular.y == self.FRAME_EE:
            self.teleop_frame = "ee"
            self.get_logger().info("TO Frame → END EFFECTOR")
            return
        
        
        vel_ee = np.array([msg.linear.x, msg.linear.y, msg.linear.z])
        velocity_magnitude = np.linalg.norm(vel_ee)
        
        if velocity_magnitude < 0.001:
            self.joint_velocities = np.zeros(3)
            return
        
        try:
            if self.kinematics.is_near_singularity(self.current_q):
                self.get_logger().warn('⚠️ Near singularity! Stopping.')
                self.joint_velocities = np.zeros(3)
                return
            
            joint_vel = self.kinematics.ee_velocity_to_qdot(
                self.current_q, vel_ee, frame=self.teleop_frame
            )
            
            joint_vel *= 0.5
            vel_mag = np.linalg.norm(joint_vel)
            if vel_mag > 1.0:
                joint_vel *= 1.0 / vel_mag
            
            self.joint_velocities = joint_vel
            
            if velocity_magnitude > 0.01:
                self.get_logger().info(
                    f'TO: vel_ee=[{vel_ee[0]:.2f}, {vel_ee[1]:.2f}, {vel_ee[2]:.2f}] → '
                    f'q_dot=[{joint_vel[0]:.2f}, {joint_vel[1]:.2f}, {joint_vel[2]:.2f}]',
                    throttle_duration_sec=0.5
                )
        
        except Exception as e:
            self.get_logger().error(f'Jacobian error: {e}')
            self.joint_velocities = np.zeros(3)
    
    
    def custom_target_callback(self, request, response):
        if self.mode != "IPK":
            response.success = False
            response.message = "Not in IPK mode"
            return response
        
        target_pos = [request.target.x, request.target.y, request.target.z]
        
        msg = PoseStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'link_0'
        msg.pose.position.x = target_pos[0]
        msg.pose.position.y = target_pos[1]
        msg.pose.position.z = target_pos[2]
        msg.pose.orientation.w = 1.0
        
        self.target_sub.callback(msg)
        response.success = True
        response.message = f"Target sent: {target_pos}"
        return response
    
    
    def target_callback(self, msg):
        if self.mode == "IPK":
            self.handle_ipk_target(msg)
    
    def handle_ipk_target(self, target_msg):
        target_pos = [
            target_msg.pose.position.x,
            target_msg.pose.position.y,
            target_msg.pose.position.z
        ]
        
        self.get_logger().info(
            f'IPK: Target [{target_pos[0]:.3f}, {target_pos[1]:.3f}, {target_pos[2]:.3f}]'
        )
        
        solution = self.kinematics.inverse_kinematics(target_pos, self.current_q)
        
        if solution is not None:
            self.get_logger().info(
                f'✓ IK Solution: [{solution[0]:.3f}, {solution[1]:.3f}, {solution[2]:.3f}]'
            )
            self.publish_status("IK SUCCESS")
            self.move_to_position(solution)
        else:
            self.get_logger().warn('✗ No IK solution')
            self.publish_status("IK FAILED")

    
    def mode_select_callback(self, request, response):
        mode = request.mode.data
        
        if mode not in ["IDLE", "IPK", "TO", "AM"]:
            response.success = False
            self.get_logger().warn(f"Invalid mode: {mode}")
            return response
        
        old_mode = self.mode
        self.mode = mode
        response.success = True
        
        if mode == "TO":
            self.joint_velocities = np.zeros(3)
        elif mode == "IPK":
            self.is_moving = False
        elif mode == "AM":
            self.am_waiting = False
            self.is_moving = False
            self.get_logger().info("AM Mode: Autonomous random movement enabled.")
        
        self.get_logger().info(f"Mode: {old_mode} → {mode}")
        self.publish_status(f"Mode: {mode}")
        
        return response
    
    def ik_service_callback(self, request, response):
        target_pos = [request.target.x, request.target.y, request.target.z]
        
        self.get_logger().info(f'IK Service: [{target_pos[0]:.3f}, {target_pos[1]:.3f}, {target_pos[2]:.3f}]')
        
        solution = self.kinematics.inverse_kinematics(target_pos, self.current_q)
        
        if solution is not None:
            response.success = True
            response.message = "IK solution found"
            response.solution = solution.tolist()
            self.get_logger().info(
                f'✓ Solution: [{solution[0]:.3f}, {solution[1]:.3f}, {solution[2]:.3f}]'
            )
        else:
            response.success = False
            response.message = "No IK solution"
            response.solution = []
            self.get_logger().warn('✗ No solution')
        
        return response

    
    def move_to_position(self, q):
        self.target_q = np.array(q)
        self.is_moving = True
        
        distance = np.linalg.norm(self.target_q - self.current_q)
        self.get_logger().info(
            f'Moving to: [{q[0]:.3f}, {q[1]:.3f}, {q[2]:.3f}] (distance: {distance:.3f} rad)'
        )
    
    def reset_position(self):
        self.current_q = self.safe_q.copy()
        self.joint_velocities = np.zeros(3)
        self.is_moving = False
        self.publish_joint_state()
        self.get_logger().info("✔ Robot reset to safe configuration.")
    
    def publish_joint_state(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['link_0_to_link_1', 'link_1_to_link_2', 'link_2_to_link_3']
        msg.position = self.current_q.tolist()
        self.joint_pub.publish(msg)
    
    def publish_status(self, message):
        msg = String()
        msg.data = message
        self.status_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = controller()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__=='__main__':
    main()