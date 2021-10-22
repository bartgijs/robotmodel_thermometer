import rclpy
from .temperature_conversions import *
from rclpy.node import Node
from std_msgs.msg import Float32
from .constants import Constants

class EnvironMent(Node):
    environment_temp = Constants.ambient_temperature
    temperature = 20.0

    def __init__(self):
        publisherTimerPeriod = Constants.environment_interval  # seconds
        temperatureTimerPeriod = 1.0  # seconds

        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Float32, Constants.topic_stimuli, 10)
        self.timer = self.create_timer(publisherTimerPeriod, self.pub_timer_callback)
        self.timer = self.create_timer(temperatureTimerPeriod, self.temp_timer_callback)
        self.subscription = self.create_subscription(Float32, Constants.topic_actions, self.sub_callback, 10)
        self.subscription  # prevent unused variable warning
    
    def pub_timer_callback(self):
        msg = Float32()
        msg.data = self.temperature
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

    def sub_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        self.temperature = convert_power_to_temp(msg.data, self.temperature)
        self.get_logger().info('Actual temp: "%s"' % self.temperature)
    
    def temp_timer_callback(self):
        self.temperature = self.temperature - 0.2
        if self.temperature < self.environment_temp:
            self.temperature = float(self.environment_temp)
        self.get_logger().info('Reducing temperature: "%s"' % self.temperature)


def main():
    rclpy.init()

    minimal_publisher = EnvironMent()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
