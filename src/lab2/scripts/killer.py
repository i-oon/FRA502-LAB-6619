#!/usr/bin/python3

from lab2.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Int64

import numpy as np

class killer(Node):
    def __init__(self):
        super().__init__('killer')
        
        self.count = 0
        self.turtle1 = []
        self.turtle2 = []
        
        
        self.create_subscription(Pose, '/turtle1/pose', self.turtle1_pose_callback, 10)
        self.create_subscription(Int64, '/turtle1/pizza_count', self.count_callback, 10)
        self.create_subscription(Pose, '/turtle2/pose', self.turtle2_pose_callback, 10)
        self.cmdvel_pub = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.spawn_turtle2_client = self.create_client(Spawn, '/spawn_turtle')
        self.kill_client = self.create_client(Kill, '/remove_turtle')
        
        self.spawn_turtle2()

        
        self.create_timer(0.01, self.timer_callback)
        
        self.flag_count = 0
    
    def count_callback(self, msg):
        self.count = msg.data
        
    def kill_turtle1(self):
        kill_request = Kill.Request()
        kill_request.name = 'turtle1'
        self.kill_client.call_async(kill_request)
        
    def spawn_turtle2(self):
        spawn_request = Spawn.Request()
        spawn_request.x = 5.44
        spawn_request.y = 5.44
        spawn_request.theta = 0.0
        spawn_request.name = "turtle2"
        self.spawn_turtle2_client.call_async(spawn_request)
    
    def cmd_vel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.z = w
        self.cmdvel_pub.publish(msg)

    def turtle2_pose_callback(self, msg):
        self.turtle2_pose = Pose()
        self.turtle2_pose.x = msg.x
        self.turtle2_pose.y = msg.y
        self.turtle2_pose.theta = msg.theta
    
    def turtle1_pose_callback(self, msg):
        self.turtle1_pose = Pose()
        self.turtle1_pose.x = msg.x
        self.turtle1_pose.y = msg.y
        self.turtle1_pose.theta = msg.theta
        self.turtle1 = np.array([self.turtle1_pose.x, self.turtle1_pose.y, self.turtle1_pose.theta])
       
    def timer_callback(self):
        
        # if self.count > 4 and self.flag_count == 0:
        #     self.flag_count = 1
        # elif self.flag_count == 1:
        #     self.spawn_turtle2()
            
        #     self.flag_count = 3
        
        if self.count > 4 :
            if self.turtle1 is [] and self.turtle2 is []:
                self.cmd_vel(0.0, 0.0)
                return
            
            dx = self.turtle1[0] - self.turtle2_pose.x
            dy = self.turtle1[1] - self.turtle2_pose.y
    
            linear_distance = np.sqrt(dx**2 + dy**2)
            angle = np.arctan2(dy,dx)
            error = angle - self.turtle2_pose.theta
            angular_angle = np.arctan2(np.sin(error), np.cos(error))
            self.cmd_vel(5*linear_distance, 15*angular_angle)
            
            
            if linear_distance < 0.1:
                if self.flag_count == 0:
                    self.kill_turtle1()
                    self.flag_count = 1
                self.cmd_vel(0.0, 0.0)
                

def main(args=None):
    rclpy.init(args=args)
    node = killer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
