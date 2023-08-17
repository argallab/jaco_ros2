""" Static transform publisher acquired via MoveIt 2 hand-eye calibration """
""" EYE-IN-HAND: j2n6s200_end_effector -> camera_color_optical_frame """
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    nodes = [
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output="log",
            arguments=[
                "--frame-id",
                "j2n6s200_end_effector",
                "--child-frame-id",
                "camera_color_optical_frame",
                "--x",
                "0.031061",
                "--y",
                "0.133440",
                "--z",
                "-0.147001",
                "--qx",
                "0.000156",
                "--qy",
                "-0.147002",
                "--qz",
                "0.990850",
                "--qw",
                "-0.000236",
            ],
        ),
    ]
    return LaunchDescription(nodes)
