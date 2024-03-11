import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf2_ros import TransformListener, Buffer
import numpy as np
import math
import random

class ControladorCarrinho(Node):
    def __init__(self):
        super().__init__('controlador_carrinho')

        self.current_pose = Point()
        self.current_yaw = 0.0

        self.odom_subscriber = self.create_subscription(
            Odometry,
            '/carrinho/odometry',
            self.odom_callback,
            10)
        self.vel_publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.rate = self.create_rate(10)

        self.targets = [(5.0, 7.0, 0.0), (6.0, -6.0, 0.0), (9.0, 0.0, 0.0), (-6.0, 3.0, 0.0), (-2.0, -6.0, 0.0)]
        self.target_index = 0

    def odom_callback(self, msg):
        self.current_pose = msg.pose.pose.position
        orientation_q = msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        try:
            transform = self.tf_buffer.lookup_transform("odom", "base_link", rclpy.time.Time())
            self.current_yaw = math.atan2(2.0 * (transform.transform.rotation.w * transform.transform.rotation.z + transform.transform.rotation.x * transform.transform.rotation.y), 1.0 - 2.0 * (transform.transform.rotation.y * transform.transform.rotation.y + transform.transform.rotation.z * transform.transform.rotation.z))
        except Exception as e:
            self.get_logger().error(f"Failed to lookup transform: {e}")

    def calculate_linear_velocity(self, target_pose):
        linear_velocity = Twist()
        linear_velocity.linear.x = 0.5 
        return linear_velocity

    def calculate_angular_velocity(self, target_pose):
        angular_velocity = Twist()
        target_yaw = np.arctan2(target_pose[1] - self.current_pose.y, target_pose[0] - self.current_pose.x)
        angular_velocity.angular.z = target_yaw - self.current_yaw  
        return angular_velocity

    def run(self):
        while rclpy.ok():
            random.shuffle(self.targets) 
            for target_pose in self.targets:
                target_x, target_y, target_z = target_pose
                self.get_logger().info(f"Going to target: {target_x}, {target_y}, {target_z}")

                while True:
                    distance_to_target = np.linalg.norm(np.array(target_pose) - np.array((self.current_pose.x, self.current_pose.y, self.current_pose.z)))
                    if distance_to_target < 0.1:  
                        break

                    linear_velocity = self.calculate_linear_velocity(target_pose)
                    angular_velocity = self.calculate_angular_velocity(target_pose)

                    combined_velocity = Twist()
                    combined_velocity.linear = linear_velocity.linear
                    combined_velocity.angular = angular_velocity.angular

                    self.vel_publisher.publish(combined_velocity)

                    self.rate.sleep()

def main(args=None):
    rclpy.init(args=args)
    controlador = ControladorCarrinho()
    controlador.run()
    rclpy.spin(controlador)
    rclpy.shutdown()

if __name__ == '__main__':
    main()