#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import JointState
from scipy.spatial.transform import Rotation
from LAB4.workspace_analysis import RobotKinematics
import numpy as np



class end_effector_publisher(Node):
    def __init__(self):
        super().__init__('end_effector_publisher')
        
        self.kinematics = RobotKinematics()
        
        # Subscribe
        self.joint_sub = self.create_subscription(JointState, 'joint_states', self.joint_state_callback, 10)
        # Publisher
        self.ee_pub = self.create_publisher(PoseStamped, 'end_effector', 10)
        
        self.get_logger().info('='*60)
        self.get_logger().info('End Effector Publisher initialized')
        self.get_logger().info('='*60)
        
    def joint_state_callback(self, msg):

        if len(msg.position) >= 3:
            q = list(msg.position[:3])
            pos, R = self.kinematics.get_pose(q)
            quat = Rotation.from_matrix(R).as_quat()  # [x, y, z, w]

            ee_msg = PoseStamped()
            ee_msg.header.stamp = self.get_clock().now().to_msg()
            ee_msg.header.frame_id = 'link_0'
            
            ee_msg.pose.position.x = float(pos[0])
            ee_msg.pose.position.y = float(pos[1])
            ee_msg.pose.position.z = float(pos[2])
            
            ee_msg.pose.orientation.x = float(quat[0])
            ee_msg.pose.orientation.y = float(quat[1])
            ee_msg.pose.orientation.z = float(quat[2])
            ee_msg.pose.orientation.w = float(quat[3])
            
            self.ee_pub.publish(ee_msg)
            

def main(args=None):
    rclpy.init(args=args)
    node = end_effector_publisher()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()