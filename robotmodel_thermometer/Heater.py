import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from .constants import Constants
import numpy as np

class Heater(Node):
    def __init__(self):

        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Float32, Constants.topic_actions, 10)
        self.subscription = self.create_subscription(Float32, Constants.topic_commands, self.sub_callback, 10)
        self.subscription  # prevent unused variable warning

    def sub_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        
        mu, sigma = 0, Constants.heater_delta # mean and standard deviation
        noise = float(np.random.normal(mu, sigma, 1))

        msg2 = Float32()
        msg2.data = msg.data + noise
        self.publisher_.publish(msg2)
        self.get_logger().info('Publishing: "%s"' % msg2.data)


def main():
    rclpy.init()

    minimal_publisher = Heater()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
