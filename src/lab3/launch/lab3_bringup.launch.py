from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    launch_description = LaunchDescription()
    
    turtlesim_node = Node(
        package='turtlesim_plus',
        namespace='',
        executable='turtlesim_plus_node.py',
        name='turtlesim_plus'
    )
    
    turtle_x = 'XXXX'
    turtle_y = 'YYYY'
    
    eater_node = Node(
        package='lab3',
        namespace = turtle_x,
        executable = 'eater.py',
        name='eater',
        parameters=[{'sampling_frequency': 100.0},
                    {'turtle_x': turtle_x},
                    {'turtle_y': turtle_y}
                    ],
        output = 'screen'
    )
    
    killer_node = Node(
        package = 'lab3',
        namespace = turtle_y,
        executable = 'killer.py',
        name='killer',
        parameters=[{'sampling_frequency': 100.0},
                    {'turtle_x': turtle_x},
                    {'turtle_y': turtle_y}
                    ],
        output = 'screen'
    )
    
    launch_description.add_action(turtlesim_node)
    launch_description.add_action(eater_node)
    launch_description.add_action(killer_node)
    
    kill_turtle1 = ExecuteProcess(
            cmd = [
                'ros2 service call',
                '/remove_turtle',
                'turtlesim/srv/Kill',
                "'name: 'turtle1''"
            ],
            shell=True
        )
    spawn_xxxx = ExecuteProcess(
            cmd = [
                'ros2 service call',
                '/spawn_turtle',
                'turtlesim/srv/Spawn',
                f'"{{x: 5.4, y: 5.4, theta: 0.0, name: {turtle_x}}}"'
            ],
            shell=True
        )
    
    spawn_yyyy = ExecuteProcess(
            cmd = [
                'ros2 service call',
                '/spawn_turtle',
                'turtlesim/srv/Spawn',
                f'"{{x: 5.4, y: 5.4, theta: 0.0, name: {turtle_y}}}"'
            ],
            shell=True
        )
    launch_description.add_action(kill_turtle1)
    launch_description.add_action(spawn_xxxx)
    launch_description.add_action(spawn_yyyy)

    
    return launch_description