import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.get_logger().info('Sensor Publisher iniciado')

        self.sensor_publisher = self.create_publisher(Twist, 'velocidade_sensor', 10)
        self.timer = self.create_timer(1.0, self.publish_sensor_data)

    def publish_sensor_data(self):
        msg = Twist()
        msg.linear.x = random.uniform(0.0, 1.0)
        msg.linear.y = random.uniform(0.0, 1.0)
        msg.linear.z = random.uniform(0.0, 1.0)
        msg.angular.x = random.uniform(0.0, 1.0)
        msg.angular.y = random.uniform(0.0, 1.0)
        msg.angular.z = random.uniform(0.0, 1.0)
        self.sensor_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    sensor_publisher = SensorPublisher()
    rclpy.spin(sensor_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()