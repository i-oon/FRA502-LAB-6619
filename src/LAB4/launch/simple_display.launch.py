#!/usr/bin/env python3

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import os
import xacro

def generate_launch_description():
    
    # Get packages
    robot_pkg = get_package_share_directory('example_description')
    
    # Robot description
    robot_xacro_path = os.path.join(robot_pkg, 'robot', 'visual', 'my-robot.xacro')
    robot_desc_xml = xacro.process_file(robot_xacro_path).toxml()
    
    # RViz config
    rviz_path = os.path.join(robot_pkg, 'config', 'display.rviz')
    
    
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc_xml}]
    )
    
    controller = Node(
        package='LAB4',
        executable='controller.py',
        output='screen'
    )
    
    end_effector_publisher = Node(
        package='LAB4',
        executable='end_effector_publisher.py',
        output='screen'
    )
    
    random_node = Node(
        package='LAB4',
        executable='random_pose.py',
        output='screen'
    )

    teleop_jog = Node(
        package='LAB4',
        executable='teleop_jog_keyboard.py',
        output='screen',
        prefix='xterm -e',
        emulate_tty=True
    )
    
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz',
        arguments=['-d', rviz_path],
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher,
        controller,
        end_effector_publisher,
        random_node,
        teleop_jog,  # ← Added!
        rviz,
    ])