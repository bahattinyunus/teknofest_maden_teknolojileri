from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # AI Reserve Predictor (Can be run as a standalone script or node)
        # Note: In a real ROS 2 system, this would be a node that listens to requests.
        # For now, we launch the core services.

        # 1. Autonomous Navigation Node (C++)
        Node(
            package='teknofest_maden_teknolojileri',
            executable='navigation_node',
            name='navigation_node',
            output='screen'
        ),

        # 2. ISG Monitor Node (Python)
        Node(
            package='teknofest_maden_teknolojileri',
            executable='isg_monitor',
            name='isg_monitor',
            output='screen'
        ),

        # 3. Alert Node (Python)
        Node(
            package='teknofest_maden_teknolojileri',
            executable='alert_node',
            name='alert_node',
            output='screen'
        )
    ])
