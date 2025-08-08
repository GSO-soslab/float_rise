
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os

def generate_launch_description():
    # namespace for a project
    robot_name = 'float_rise_2'
    # basic vehicle name
    vehicle_name = 'float_2'

    path_to_urdf = os.path.join( 
        get_package_share_directory('float_rise_description'), 'urdf', vehicle_name, 'base.urdf' )
    with open(path_to_urdf, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            namespace=robot_name,
            # output='screen',
            parameters=[{'robot_description' : robot_desc},
                        {'frame_prefix': robot_name +'/'}],
        ),

])
