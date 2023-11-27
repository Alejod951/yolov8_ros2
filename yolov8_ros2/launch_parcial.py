import launch
import launch_ros.actions

def generate_launch_description():
    # Lanzamos el nodo img_publisher
    img_publisher_node = launch_ros.actions.Node(
        package='parcialii',
        executable='img_publisher',
    )

    # Lanzamos el nodo img_detector
    img_detector_node = launch_ros.actions.Node(
        package='parcialii',
        executable='img_detector',
    )

    # Lanzamos el nodo img_filter
    img_filter_node = launch_ros.actions.Node(
        package='parcialii',
        executable='img_filter',
    )

    # Lanzamos el nodo img_detector_filter
    img_detector_filter_node = launch_ros.actions.Node(
        package='parcialii',
        executable='img_detector_filter',
    )

    # Lanzamos el comando ros2 topic echo para el topic /video_detector
    echo_video_detector_node = launch_ros.actions.Node(
        package='ros2',
        executable='topic_echo',
        arguments=['/video_detector'],
    )

    # Lanzamos el comando ros2 topic echo para el topic /video_detector_filter
    echo_video_detector_filter_node = launch_ros.actions.Node(
        package='ros2',
        executable='topic_echo',
        arguments=['/video_detector_filter'],
    )

    # Lanzamos RViz2
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', 'parcialii/rviz.rviz'],
    )

    return launch.LaunchDescription([
        img_publisher_node,
        img_detector_node,
        img_filter_node,
        img_detector_filter_node,
        echo_video_detector_node,
        echo_video_detector_filter_node,
        rviz_node,
    ])

if __name__ == '__main__':
    launch.launch(generate_launch_description())