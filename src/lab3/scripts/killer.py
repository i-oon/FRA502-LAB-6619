#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Int64, Bool
from controller_interfaces.srv import SetParam

import numpy as np

class killer(Node):
    def __init__(self):
        super().__init__('killer')
        
        self.count = 0
        self.turtle1 = None
        self.turtle2 = None
        self.turtle2_spawned = False
        self.flag_count = 0 
        self.kp_linear = 1.0
        self.kp_angular = 10.0

        self.declare_parameter('turtle_y', 'YYYY')
        self.turtle_y = self.get_parameter('turtle_y').get_parameter_value().string_value
        self.declare_parameter('turtle_x', 'XXXX')
        self.turtle_x = self.get_parameter('turtle_x').get_parameter_value().string_value
        self.declare_parameter('sampling_frequency', 100.0)
        self.frequency = self.get_parameter('sampling_frequency').get_parameter_value().double_value

        self.create_subscription(Pose, f'/{self.turtle_x}/pose', self.turtle1_pose_callback, 10)
        # self.create_subscription(Int64, '/turtle1/pizza_count', self.count_callback, 10)
        self.create_subscription(Pose, f'/{self.turtle_y}/pose', self.turtle2_pose_callback, 10)
        self.cmdvel_pub = self.create_publisher(Twist, f'/{self.turtle_y}/cmd_vel', 10)
        self.spawn_turtle2_client = self.create_client(Spawn, '/spawn_turtle')
        self.kill_client = self.create_client(Kill, '/remove_turtle')
        
        self.create_subscription(Bool, f'/{self.turtle_x}/eat_status', self.eat_status_callback, 10)        
        self.create_service(SetParam, 'set_param', self.set_param_callback)
        
        self.create_timer(1/self.frequency, self.timer_callback)
        # self.spawn_turtle2()
        
    
            
    def set_param_callback(self, request:SetParam.Request, response:SetParam.Response):
        self.kp_linear = request.kp_linear.data
        self.kp_angular = request.kp_angular.data
        return response
    
    def eat_status_callback(self, msg):
        if msg.data:
            self.turtle2_spawned = True
        else:
            self.turtle2_spawned = False
        
    def kill_turtle1(self):
        kill_request = Kill.Request()
        kill_request.name = self.turtle_x
        self.kill_client.call_async(kill_request)
        
    # def spawn_turtle2(self):
    #     spawn_request = Spawn.Request()
    #     spawn_request.x = 5.44
    #     spawn_request.y = 5.44
    #     spawn_request.theta = 0.0
    #     spawn_request.name = "turtle2"
    #     self.spawn_turtle2_client.call_async(spawn_request)
    
    def cmd_vel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.z = w
        self.cmdvel_pub.publish(msg)

    def turtle2_pose_callback(self, msg):
        self.turtle2 = np.array([msg.x, msg.y, msg.theta])
    
    def turtle1_pose_callback(self, msg):
        self.turtle1 = np.array([msg.x, msg.y, msg.theta])
       
    def timer_callback(self):    
        if self.turtle2_spawned :
            if self.turtle1 is None or self.turtle2 is None:
                self.cmd_vel(0.0, 0.0)
                return
            
            dx = self.turtle1[0] - self.turtle2[0] 
            dy = self.turtle1[1] - self.turtle2[1] 
    
            linear_distance = np.sqrt(dx**2 + dy**2)
            angle = np.arctan2(dy,dx)
            error = angle - self.turtle2[2]
            angular_angle = np.arctan2(np.sin(error), np.cos(error))
            self.cmd_vel(self.kp_linear*linear_distance, self.kp_angular*angular_angle)
            
            if linear_distance < 0.1:
                if self.flag_count == 0:
                    self.kill_turtle1()
                    self.flag_count = 1
                self.cmd_vel(0.0, 0.0)
        else:
            self.cmd_vel(0.0, 0.0)
                

def main(args=None):
    rclpy.init(args=args)
    node = killer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
