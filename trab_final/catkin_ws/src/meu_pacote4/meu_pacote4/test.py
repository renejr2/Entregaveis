import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CustomPublisher(Node):

    def __init__(self):
        super().__init__('custom_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5  
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = self.create_twist_message()
        self.publish_twist_message(msg)

    def create_twist_message(self):
        msg = Twist()
        msg.linear.x = -4.0
        msg.linear.y = 3.0
        msg.angular.z = 2.0
        return msg

    def publish_twist_message(self, msg):
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    custom_publisher = CustomPublisher()

    try:
        rclpy.spin(custom_publisher)
    except KeyboardInterrupt:
        pass

    custom_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()