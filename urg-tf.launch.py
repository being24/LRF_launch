from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="urg_node",
                executable="urg_node_driver",
                namespace="urg30",
                parameters=[
                    {"serial_port": "/dev/ttyACM0", "laser_frame_id": "urg30_laser"}
                ],
                remappings=[
                    ("scan", "scan"),
                ],
            ),
            Node(
                package="urg_node",
                executable="urg_node_driver",
                namespace="f01",
                parameters=[
                    {"serial_port": "/dev/ttyACM1", "laser_frame_id": "f01_laser"}
                ],
                remappings=[
                    ("scan", "scan"),
                ],
            ),
            Node(
                package="tf2_ros",
                executable="static_transform_publisher",
                arguments=["0", "10", "0", "0", "0", "0", "map", "urg30_laser"],
            ),
            Node(
                package="tf2_ros",
                executable="static_transform_publisher",
                arguments=["0", "5", "0", "0", "0", "1", "map", "f01_laser"],
            ),
        ],
    )
