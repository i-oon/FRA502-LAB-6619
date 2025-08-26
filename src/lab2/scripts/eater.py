#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point, PoseStamped
from turtlesim.msg import Pose
from turtlesim_plus_interfaces.srv import GivePosition
from std_srvs.srv import Empty
from std_msgs.msg import Int64


import numpy as np

class eater(Node):
    def __init__(self):
        super().__init__('eater')
        self.create_subscription(Pose, '/turtle1/pose', self.turtle_pose_callback, 10)
        self.create_subscription(Point, '/mouse_position', self.mouse_pose_callback, 10 )
        self.create_subscription(PoseStamped, '/goal_pose', self.goal_callback, 10 )
        self.spawn_pizza_client = self.create_client(GivePosition, '/spawn_pizza')
        self.eat_pizza_client = self.create_client(Empty, '/turtle1/eat')
        self.cmdvel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pizza_count_pub = self.create_publisher(Int64, '/turtle1/pizza_count', 10)
        
        
        self.create_timer(0.01, self.timer_callback)
        self.waypoint = []
        self.count = 0
        self.pizza_count_callback(self.count)
        
    def goal_callback(self, msg):
        goal_pose = np.array([msg.pose.position.x + 5.44, msg.pose.position.y + 5.44])
        # print('goal_pose')
        self.waypoint.append(goal_pose)
        if self.count < 5:
            self.spawn_pizza(goal_pose[0], goal_pose[1])
        
        
    
    def pizza_count_callback(self, count):
        msg = Int64()
        msg.data = count
        self.pizza_count_pub.publish(msg)
            
        
        
    def eat_pizza(self):
        eat_request = Empty.Request()
        return self.eat_pizza_client.call_async(eat_request)    
    
    def spawn_pizza(self, x, y):
        spawn_request = GivePosition.Request()
        spawn_request.x = x
        spawn_request.y = y
        return self.spawn_pizza_client.call_async(spawn_request)
    
    def cmd_vel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.z = w
        self.cmdvel_pub.publish(msg)
        
    def mouse_pose_callback(self, msg):
        mouse = np.array([msg.x, msg.y])
        self.waypoint.append(mouse)
        if self.count < 5:
            self.spawn_pizza(mouse[0], mouse[1])
        
    def turtle_pose_callback(self, msg):
        self.turtle_pose = Pose()
        self.turtle_pose.x = msg.x
        self.turtle_pose.y = msg.y
        self.turtle_pose.theta = msg.theta
    
    
    def timer_callback(self):
        if not self.waypoint or self.turtle_pose is None:
            self.cmd_vel(0.0, 0.0)
            return

        dx = self.waypoint[0][0] - self.turtle_pose.x
        dy = self.waypoint[0][1] - self.turtle_pose.y
        linear_distance = np.sqrt(dx**2 + dy**2)
        angle = np.arctan2(dy,dx)
        error = angle - self.turtle_pose.theta
        angular_angle = np.arctan2(np.sin(error), np.cos(error))

        self.cmd_vel(10*linear_distance, 15*angular_angle)
        
        # if angular_angle > 
        
        if linear_distance < 0.1 :
            self.cmd_vel(0.0, 0.0)
            self.count += 1
            self.eat_pizza()
            self.pizza_count_callback(self.count)
            self.waypoint.pop(0)
                
            
            
            
            
            

            
    

def main(args=None):
    rclpy.init(args=args)
    node = eater()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
