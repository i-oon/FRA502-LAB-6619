#!/usr/bin/python3

from lab2.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry 
from tf2_ros import TransformBroadcaster
from tf_transformations import quaternion_from_euler
from turtlesim.msg import Pose
import numpy as np

class turtlesim_pose(Node):
    def __init__(self):
        super().__init__('turtlesim_pose')

        self.turtle1_pose = np.array([0.0, 0.0, 0.0])
        self.turtle2_pose = np.array([0.0, 0.0, 0.0])
        self.create_subscription(Pose, '/turtle1/pose', lambda msg: self.pose_callback(msg, 'turtle1', 'turtle1'), 10)
        self.create_subscription(Pose, '/turtle2/pose', lambda msg: self.pose_callback(msg, 'turtle2', 'turtle2'), 10)

        self.odom1_publisher = self.create_publisher(Odometry, '/odom1', 10)
        self.odom2_publisher = self.create_publisher(Odometry, '/odom2', 10)

        self.tf_broadcaster = TransformBroadcaster(self)
        
    def pose_callback(self, msg, turtle_name, child_frame_id):
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        self.turtle1_pose = np.array([msg.x, msg.y, msg.theta])
        x = self.turtle1_pose[0]
        y = self.turtle1_pose[1]
        theta = self.turtle1_pose[2]
        
        odom_msg.header.frame_id = 'odom'
        odom_msg.child_frame_id = child_frame_id
        odom_msg.pose.pose.position.x = x - 5.44
        odom_msg.pose.pose.position.y = y - 5.44
        q =  quaternion_from_euler(0,0,theta)
        
        odom_msg.pose.pose.orientation.x = q[0]
        odom_msg.pose.pose.orientation.y = q[1]
        odom_msg.pose.pose.orientation.z = q[2]
        odom_msg.pose.pose.orientation.w = q[3]
        
        if turtle_name == 'turtle1':
            self.odom1_publisher.publish(odom_msg) 
        else:
            self.odom2_publisher.publish(odom_msg) 
        
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = child_frame_id
        
        t.transform.translation.x = self.turtle1_pose[0]- 5.44
        t.transform.translation.y = self.turtle1_pose[1]- 5.44
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        
        self.tf_broadcaster.sendTransform(t)
        

def main(args=None):
    rclpy.init(args=args)
    node = turtlesim_pose()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
