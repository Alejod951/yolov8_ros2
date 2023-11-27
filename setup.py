from setuptools import setup

package_name = 'yolov8_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alejo',
    maintainer_email='alejo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'img_publi = yolov8_ros2.image_publisdete:main',
	        'img_detector = yolov8_ros2.image_detector:main',
            'img_filter = yolov8_ros2.filter_HPF:main',
            'img_detector_filter = yolov8_ros2.image_detector_filter:main',
            'img_filter2 = yolov8_ros2.filter_Prom:main',
            'img_filter3 = yolov8_ros2.filter_Median:main',
            'img_filter4 = yolov8_ros2.filtro_gauss:main',
        ],
    },
)
