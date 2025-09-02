#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point, PoseStamped
from turtlesim.msg import Pose
from turtlesim_plus_interfaces.srv import GivePosition
from std_srvs.srv import Empty
from std_msgs.msg import Int64, Bool
from controller_interfaces.srv import SetParam, SetMaxPizza

import numpy as np

class eater(Node):
    def __init__(self):
        super().__init__('eater')
        
        self.declare_parameter('turtle_y', 'YYYY')
        self.turtle_y = self.get_parameter('turtle_y').get_parameter_value().string_value
        self.declare_parameter('turtle_x', 'XXXX')
        self.turtle_x = self.get_parameter('turtle_x').get_parameter_value().string_value
        self.declare_parameter('sampling_frequency', 100.0)
        self.frequency = self.get_parameter('sampling_frequency').get_parameter_value().double_value
        
        self.create_subscription(Pose, f'/{self.turtle_x}/pose', self.turtle_pose_callback, 10)
        self.create_subscription(Point, '/mouse_position', self.mouse_pose_callback, 10 )
        self.create_subscription(PoseStamped, '/goal_pose', self.goal_callback, 10 )
        self.spawn_pizza_client = self.create_client(GivePosition, '/spawn_pizza')
        self.eat_pizza_client = self.create_client(Empty, f'/{self.turtle_x}/eat')
        self.cmdvel_pub = self.create_publisher(Twist, f'/{self.turtle_x}/cmd_vel', 10)
        self.pizza_count_pub = self.create_publisher(Int64, f'/{self.turtle_x}/pizza_count', 10)
        self.eat_status_pub = self.create_publisher(Bool, f'/{self.turtle_x}/eat_status', 10)
        
        
        self.create_service(SetParam, 'set_param', self.set_param_callback)
        self.create_service(SetMaxPizza, 'set_max_pizza', self.set_max_pizza_callback)
        
        self.create_timer(1/self.frequency, self.timer_callback)
        self.waypoint = []
        self.count_eat = 0
        self.count_spawn = 0
        self.turtle_pose = None
        self.kp_linear = 5.0
        self.kp_angular = 15.0
        self.max_pizza = 5
        
        self.log = 'failed'
        self.pizza_count_callback(self.count_eat)
    
    def eat_status_callback(self, status):
        msg = Bool()
        msg.data = status
        self.eat_status_pub.publish(msg)
    
    def set_max_pizza_callback(self, request:SetMaxPizza.Request, response:SetMaxPizza.Response):
        if request.max_pizza.data > self.max_pizza:
            self.max_pizza = request.max_pizza.data
            response.log.data  = 'success'
        else:
            response.log.data  = 'failed'
            
        return response
    
    def set_param_callback(self, request:SetParam.Request, response:SetParam.Response):
        self.kp_linear = request.kp_linear.data
        self.kp_angular = request.kp_angular.data
        return response
        
    def goal_callback(self, msg):
        goal_pose = np.array([msg.pose.position.x + 5.44, msg.pose.position.y + 5.44])
        self.waypoint.append(goal_pose)
        if self.count_eat < self.max_pizza :
            self.eat_status_callback(False)
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
        self.count_spawn += 1
    
        return self.spawn_pizza_client.call_async(spawn_request)
    
    def cmd_vel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = w
        self.cmdvel_pub.publish(msg)
        
    def mouse_pose_callback(self, msg):
        mouse = np.array([msg.x, msg.y])
        if self.count_eat < self.max_pizza:
            if self.max_pizza > self.count_spawn:
                self.spawn_pizza(mouse[0], mouse[1])
                self.waypoint.append(mouse)
            self.eat_status_callback(False)
        else:
            self.waypoint = [mouse]
            self.eat_status_callback(True)
            
        
    def turtle_pose_callback(self, msg):
        self.turtle_pose = np.array([msg.x,msg.y,msg.theta])

    
    def timer_callback(self):
        
        
        if not self.waypoint or self.turtle_pose is None:
            self.cmd_vel(0.0, 0.0)
            self.get_logger().info(f"{self.count_eat}, {self.count_spawn}")
            
            return
        # print(self.max_pizza)
        self.get_logger().info(f"{self.count_eat}, {self.count_spawn}")
        dx = self.waypoint[0][0] - self.turtle_pose[0]
        dy = self.waypoint[0][1] - self.turtle_pose[1]
        linear_distance = np.sqrt(dx**2 + dy**2)
        angle = np.arctan2(dy,dx)
        error = angle - self.turtle_pose[2]
        angular_angle = np.arctan2(np.sin(error), np.cos(error))

        self.cmd_vel(self.kp_linear*linear_distance, self.kp_angular*angular_angle)   
        
        if linear_distance < 0.1 :
            self.cmd_vel(0.0, 0.0)
            if self.count_eat < self.max_pizza:
                self.eat_status_callback(False)
                self.eat_pizza()
                self.count_eat += 1
                self.pizza_count_callback(self.count_eat)
            else:
                self.eat_status_callback(True)
            self.waypoint.pop(0)
                
                
            

def main(args=None):
    rclpy.init(args=args)
    node = eater()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
