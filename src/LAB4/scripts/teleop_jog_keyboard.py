#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseStamped
from robot_interfaces.srv import ModeSelect, RandomEndEffector
from LAB4.workspace_analysis import RobotKinematics
import numpy as np

import sys
import termios
import tty
import select

KEY_UI = r"""
==================== ADVANCED TELEOP ====================
MODE SELECTION:
  1        →  IDLE mode
  2        →  IPK mode (Inverse Kinematics)
  3        →  TO mode (Teleoperation)
  4        →  AM mode (Auto Mode)
  
IPK TARGET COMMANDS:
  T        →  Generate random target
  C        →  Input custom target coordinates

MOVEMENT (TO mode only):
  W / S    →  X-axis forward / backward
  A / D    →  Y-axis left / right
  Q / E    →  Z-axis up / down
  SPACE    →  STOP

FRAME CONTROL (TO mode):
  F        →  Switch to WORLD frame
  G        →  Switch to END-EFFECTOR frame

UTILITIES:
  R        →  RESET robot to safe pose
  H        →  Show this help
  Ctrl+C   →  Quit teleop
=========================================================
"""

class TeleopJogKeyboard(Node):

    def __init__(self):
        super().__init__('teleop_jog_keyboard')
        
        self.kinematics = RobotKinematics()

        # Publishers
        self.vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.target_pub = self.create_publisher(PoseStamped, '/target', 10)
        
        # Service clients
        self.mode_client = self.create_client(ModeSelect, 'mode_select')
        self.random_pose_client = self.create_client(RandomEndEffector, 'random_pose')
        
        
        # State
        self.speed = 0.3
        self.current_mode = "UNKNOWN"
        
        # Wait for services
        self.get_logger().info("Waiting for services...")
        self.mode_client.wait_for_service(timeout_sec=5.0)
        self.random_pose_client.wait_for_service(timeout_sec=5.0)
        
        self.get_logger().info(KEY_UI)
        
        # Save terminal settings
        self.settings = termios.tcgetattr(sys.stdin)

    def get_key(self, timeout=0.05):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], timeout)
        key = None
        if rlist:
            key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key
    
    def get_input(self, prompt):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        try:
            return input(prompt)
        finally:
            pass

    def publish_twist(self, x=0.0, y=0.0, z=0.0, angular_x=0.0, angular_y=0.0):
        msg = Twist()
        msg.linear.x = float(x)
        msg.linear.y = float(y)
        msg.linear.z = float(z)
        msg.angular.x = float(angular_x)
        msg.angular.y = float(angular_y)
        self.vel_pub.publish(msg)
    
    def publish_target(self, x, y, z):
        msg = PoseStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'link_0'
        msg.pose.position.x = float(x)
        msg.pose.position.y = float(y)
        msg.pose.position.z = float(z)
        msg.pose.orientation.w = 1.0
        self.target_pub.publish(msg)
        self.get_logger().info(f"✓ Target sent: [{x:.3f}, {y:.3f}, {z:.3f}]")

    def call_mode_service(self, mode):
        if not self.mode_client.service_is_ready():
            self.get_logger().warn("Mode service not available")
            return
        
        req = ModeSelect.Request()
        req.mode.data = mode
        
        future = self.mode_client.call_async(req)
        rclpy.spin_until_future_complete(self, future, timeout_sec=1.0)
        
        if future.done():
            response = future.result()
            if response.success:
                self.current_mode = mode
                self.get_logger().info(f"✓ Mode switched to: {mode}")
            else:
                self.get_logger().warn(f"✗ Failed to switch to {mode}")

    def call_random_pose(self):
        """Request random target pose"""
        if not self.random_pose_client.service_is_ready():
            self.get_logger().warn("Random pose service not available")
            return
        
        req = RandomEndEffector.Request()
        future = self.random_pose_client.call_async(req)
        rclpy.spin_until_future_complete(self, future, timeout_sec=1.0)
        
        if future.done():
            response = future.result()
            if response.success:
                pos = response.position
                self.get_logger().info(f"✓ Random target: [{pos.x:.3f}, {pos.y:.3f}, {pos.z:.3f}]")
    
    def input_custom_target(self):
        self.get_logger().info("")
        self.get_logger().info("="*50)
        self.get_logger().info("CUSTOM TARGET INPUT")
        self.get_logger().info("Workspace bounds (link_0 frame):")
        self.get_logger().info(f"  X: [{self.kinematics.x_min:.2f}, {self.kinematics.x_max:.2f}] m")
        self.get_logger().info(f"  Y: [{self.kinematics.y_min:.2f}, {self.kinematics.y_max:.2f}] m")
        self.get_logger().info(f"  Z: [{self.kinematics.z_min:.2f}, {self.kinematics.z_max:.2f}] m")
        self.get_logger().info("="*50)
        
        try:
            x_str = self.get_input("Enter X coordinate (m): ")
            y_str = self.get_input("Enter Y coordinate (m): ")
            z_str = self.get_input("Enter Z coordinate (m): ")
            
            x = float(x_str)
            y = float(y_str)
            z = float(z_str)
            
            x_valid = self.kinematics.x_min <= x <= self.kinematics.x_max
            y_valid = self.kinematics.y_min <= y <= self.kinematics.y_max
            z_valid = self.kinematics.z_min <= z <= self.kinematics.z_max
            all_valid = x_valid and y_valid and z_valid
            
            # Show validation
            self.get_logger().info("")
            self.get_logger().info("Validation:")
            self.get_logger().info(f"  X = {x:7.3f}  {'✓ OK' if x_valid else '✗ OUT OF BOUNDS'}")
            self.get_logger().info(f"  Y = {y:7.3f}  {'✓ OK' if y_valid else '✗ OUT OF BOUNDS'}")
            self.get_logger().info(f"  Z = {z:7.3f}  {'✓ OK' if z_valid else '✗ OUT OF BOUNDS'}")
            
            if not all_valid:
                self.get_logger().warn("")
                self.get_logger().warn("="*50)
                self.get_logger().warn("WARNING: TARGET OUTSIDE WORKSPACE!")
                
                if not x_valid:
                    self.get_logger().warn(f"  X: {x:.3f} not in [{self.kinematics.x_min:.2f}, {self.kinematics.x_max:.2f}]")
                if not y_valid:
                    self.get_logger().warn(f"  Y: {y:.3f} not in [{self.kinematics.y_min:.2f}, {self.kinematics.y_max:.2f}]")
                if not z_valid:
                    self.get_logger().warn(f"  Z: {z:.3f} not in [{self.kinematics.z_min:.2f}, {self.kinematics.z_max:.2f}]")
                
                self.get_logger().warn("="*50)
                
                confirm = self.get_input("Send anyway? (y/n): ")
                if confirm.lower() != 'y':
                    self.get_logger().info("Target cancelled")
                    return
                
                self.get_logger().warn("Sending out-of-workspace target...")
            else:
                self.get_logger().info("✓ Target within workspace")
            
            self.get_logger().info(f"Sending target: [{x:.3f}, {y:.3f}, {z:.3f}]")
            self.publish_target(x, y, z)
            
        except ValueError:
            self.get_logger().error("")
            self.get_logger().error("="*50)
            self.get_logger().error("INVALID INPUT!")
            self.get_logger().error("Please enter numeric values")
            self.get_logger().error("="*50)
        except KeyboardInterrupt:
            self.get_logger().info("")
            self.get_logger().info("Input cancelled")
        

    def check_mode(self, required_mode, command_name):
        if self.current_mode != required_mode:
            self.get_logger().warn(
                f"!!!  '{command_name}' only available in {required_mode} mode "
                f"(current: {self.current_mode})"
            )
            return False
        return True

    def run(self):
        try:
            while rclpy.ok():
                key = self.get_key()

                if key is None:
                    continue

                key_lower = key.lower()

                # Ctrl+C
                if key == '\x03':
                    raise KeyboardInterrupt
                
                # ========== MODE SELECTION (always available) ==========
                if key == '1':
                    self.call_mode_service("IDLE")
                elif key == '2':
                    self.call_mode_service("IPK")
                elif key == '3':
                    self.call_mode_service("TO")
                elif key == '4':
                    self.call_mode_service("AM")
                
                # ========== UNIVERSAL COMMANDS ==========
                elif key_lower == 'r':
                    self.publish_twist(angular_x=-999.0)
                    self.get_logger().info("↻ RESET to safe pose")
                elif key_lower == 'h':
                    self.get_logger().info(KEY_UI)
                
                # ========== IPK MODE COMMANDS ==========
                elif key_lower == 't':
                    if self.check_mode("IPK", "Random target (T)"):
                        self.call_random_pose()
                
                elif key_lower == 'c':
                    if self.check_mode("IPK", "Custom target (C)"):
                        self.input_custom_target()
                
                # ========== TO MODE COMMANDS ==========
                elif key_lower in ['w', 's', 'a', 'd', 'q', 'e']:
                    if self.check_mode("TO", "Movement"):
                        if key_lower == 'w':
                            self.publish_twist(x=self.speed)
                        elif key_lower == 's':
                            self.publish_twist(x=-self.speed)
                        elif key_lower == 'a':
                            self.publish_twist(y=self.speed)
                        elif key_lower == 'd':
                            self.publish_twist(y=-self.speed)
                        elif key_lower == 'q':
                            self.publish_twist(z=self.speed)
                        elif key_lower == 'e':
                            self.publish_twist(z=-self.speed)
                
                elif key == ' ':
                    if self.check_mode("TO", "STOP"):
                        self.publish_twist()
                
                elif key_lower == 'f':
                    if self.check_mode("TO", "Frame switch (F)"):
                        self.publish_twist(angular_y=1.0)
                        self.get_logger().info("Frame → WORLD")
                
                elif key_lower == 'g':
                    if self.check_mode("TO", "Frame switch (G)"):
                        self.publish_twist(angular_y=-1.0)
                        self.get_logger().info("Frame → END-EFFECTOR")

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
            self.get_logger().info("Teleop terminated.")


def main():
    rclpy.init()
    node = TeleopJogKeyboard()
    
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
