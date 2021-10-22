from functools import _CacheInfo
import rclpy, random
from .constants import *
from .temperature_conversions import *
from rclpy.node import Node
from std_msgs.msg import Float32
import numpy as np

listen_topic = Constants.topic_percepts
publish_topic = Constants.topic_commands
setpoint_topic = Constants.topic_setpoint


class RobotmodelController(Node):
    setpoint = 21
    capacity = Constants.water_volume
    belief = np.array([[Constants.start_temperature + random.uniform(-5, 5)], [0]])

    def __init__(self):
        super().__init__('Controller')

        # Create the subscription to take in the data
        self.setpoint_subscription = self.create_subscription(
            Float32,
            setpoint_topic,
            self.setpoint_listener_callback,
            10)
        self.setpoint_subscription # Prevent unused variable warning

        # Create the subscription to take in the data
        self.temperature_input_subscription = self.create_subscription(
            Float32,
            listen_topic,
            self.temperature_listener_callback,
            10)
        self.temperature_input_subscription # Prevent unused variable warning

        # Create the publisher to publish the command
        self.power_command_publisher = self.create_publisher(
            Float32,
            publish_topic,
            10)
        self.power_command_publisher # Prevent unused variable warning

    def setpoint_listener_callback(self, msg):
        self.setpoint = msg.data

    def temperature_listener_callback(self, msg):
        measurement = convert_fahrenheit_to_celsius(msg.data)

        # TODO: Update belief based on the Kalman filter

        # TODO: Calculate wattage output given a temperature difference from the setpoint

        wattage = 200

        if wattage > Constants.max_output_power:
            wattage = Constants.max_output_power

        if wattage < 0:
            wattage = 0

        self.publish(float(wattage))

    def publish(self, power_command):
        msg = Float32()
        msg.data = power_command
        self.publisher.publish(msg)

    def kalman_filtering(self):
        # u_t = A_t u_{t-1}
        self.belief[0][0] = 

        R_t = np.array([[Constants.sensor_delta], [Constants.heater_delta]]) @ np.array([[Constants.sensor_delta, Constants.heater_delta]])
        pass


def main(args=None):
    rclpy.init(args=args)

    controller = RobotmodelController()
    controller.kalman_filtering()

    # print("Controller started:")
    # print("   Listening on /", listen_topic, sep="")
    # print("   Publishing on /", publish_topic, sep="")

    # rclpy.spin(controller)

    # controller.destroy_node()
    # rclpy.shutdown()

if __name__ == '__main__':
    main()
