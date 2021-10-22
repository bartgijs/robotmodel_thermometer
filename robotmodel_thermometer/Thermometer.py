import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
import math
import constants


#Publisher
class Thermometer(Node):

    Temperature = 20

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Float32, 'topic', 10)
        self.i = 0
        self.time = 0
        self.min = 20
        self.range = 15
        self.delta = constants.Constants.sensor_delta

        self.subscription = self.create_subscription(
            Float32,
            constants.topic_stimuli,
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def measure(self):
        temperature = math.sin(2 * self.delta * self.time) + \
            math.sin(math.pi * self.delta * self.time)
        self.time += 1
  #      return self.min + self.range * temperature


    def listener_callback(self, msg):
        self.get_logger().info('temperature is "%s" ' %  self.min + self.range * {msg.data}, 'Farenheid')

        sg = Float32()
        msg.data = self.Temperature
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
        

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = Thermometer()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()






##van Celcius naar Farenheid --> C = (F-32)/1.8















#  def __init__(self):
#         super().__init__('minimal_publisher')
#         self.publisher_ = self.create_publisher(String, 'topic', 10)
        
#         self.timer = self.create_timer(timer_period, self.timer_callback)
#         self.i = 0

#     def timer_callback(self):
#         msg = String()
#         msg.data = 'Hello World: %d' % self.i
#         self.publisher_.publish(msg)
#         self.get_logger().info('Publishing: "%s"' % msg.data)
#         self.i += 1

#     def lisener_callback(self):
#         msg = String()

# def main():
#     print('Hi from robotmodel_thermometer : Thermometer')

# Raw_Temp =              #Variable read out of the Environment

# Temp 


# if __name__ == '__main__':
#     main()
