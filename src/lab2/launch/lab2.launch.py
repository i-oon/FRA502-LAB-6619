from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    launch_description = LaunchDescription()
    
    
    turtlesim_plus_node = Node(
        package='turtlesim_plus',
        namespace='',
        executable='turtlesim_plus_node.py',
        name='turtlesim_plus'
    )
    
    eater_node = Node(
        package='lab2',
        namespace='',
        executable='eater.py',
        name='eating'
    )
    
    killer_node = Node(
        package='lab2',
        namespace='',
        executable='killer.py',
        name='killing'
    )
    
    turtlesim_pose_node = Node(
        package='lab2',
        namespace='',
        executable='turtlesim_pose.py',
        name='posing'
    )
    
    # spawn_turtle = ExecuteProcess(
    #     cmd=['ros2',
    #          'service call',
    #          '/spawn ',
    #         'turtlesim/srv/Spawn ',
    #         '"{x: 2, y: 2, theta: 0.2}"'
    #         ],
    #     shell=True
    # )
    launch_description.add_action(turtlesim_plus_node)
    launch_description.add_action(eater_node)
    launch_description.add_action(killer_node)
    launch_description.add_action(turtlesim_pose_node)
    
    return launch_description