from setuptools import setup

package_name = 'robotmodel_thermometer'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Bart Gijsbertsen',
    maintainer_email='GLJ.Gijsbertsen@student.han.nl',
    description='Boiler according to the robot model: Proves ROS communication between devices',
    license='WTFPL',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'Controller = robotmodel_thermometer.Controller:main',
            'Thermometer = robotmodel_thermometer.Thermometer:main',
            'Heater = robotmodel_thermometer.Heater:main',
            'Environment = robotmodel_thermometer.Environment:main',
        ],
    },
)
