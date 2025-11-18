#!/usr/bin/python3
import rclpy
from rclpy.node import Node
import numpy as np
from geometry_msgs.msg import PoseStamped, Point, Quaternion
from LAB4.workspace_analysis import RobotKinematics
from robot_interfaces.srv import RandomEndEffector

class random_pose(Node):
    def __init__(self):
        super().__init__('random_pose')
    
        self.kinematics = RobotKinematics()
        
        self.get_logger().info('='*60)
        self.get_logger().info('WORKSPACE BOUNDS:')
        self.get_logger().info(f'  X: [{self.kinematics.x_min:.6f}, {self.kinematics.x_max:.6f}] m')
        self.get_logger().info(f'  Y: [{self.kinematics.y_min:.6f}, {self.kinematics.y_max:.6f}] m')
        self.get_logger().info(f'  Z: [{self.kinematics.z_min:.6f}, {self.kinematics.z_max:.6f}] m')
        self.get_logger().info('='*60)
        
        # Publisher
        self.target_pub = self.create_publisher(PoseStamped, 'target', 10)
        
        # Service
        self.random_service = self.create_service(RandomEndEffector,'random_pose',self.random_pose_callback)
        
        self.get_logger().info('='*60)
        self.get_logger().info('Random Node initialized')
        self.get_logger().info('Publishing: /target (timer-based)')
        self.get_logger().info('Service: /random_pose (on-demand)')
        self.get_logger().info('='*60)
    
    def generate_random_target(self):
        max_attempts = 100
        
        for _ in range(max_attempts):
            x = np.random.uniform(self.kinematics.x_min, self.kinematics.x_max)
            y = np.random.uniform(self.kinematics.y_min, self.kinematics.y_max)
            z = np.random.uniform(self.kinematics.z_min, self.kinematics.z_max)
            
            point = [x, y, z]
            
            if self.kinematics.is_in_workspace(point):
                return point
        
        return [0.0, 0.0, 0.2]
    
    def random_pose_callback(self, request:RandomEndEffector.Request, response:RandomEndEffector.Response):
        position = self.generate_random_target()
        
        # Service response
        response.position = Point()
        response.position.x = position[0]
        response.position.y = position[1]
        response.position.z = position[2]
        response.orientation = Quaternion()
        response.orientation.w = 1.0
        response.success = True
        
        # Publish to /target topic
        msg = PoseStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'link_0'
        msg.pose.position.x = position[0]
        msg.pose.position.y = position[1]
        msg.pose.position.z = position[2]
        msg.pose.orientation.w = 1.0
        self.target_pub.publish(msg)
        
        self.get_logger().info(f'Service request - Random pose: [{position[0]:.3f}, {position[1]:.3f}, {position[2]:.3f}]')
        
        return response

def main(args=None):
    rclpy.init(args=args)
    node = random_pose()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
