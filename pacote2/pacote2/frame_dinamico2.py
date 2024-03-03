import rclpy
import math
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

class FrameDinamico2(Node):
    def __init__(self):
        super().__init__('FrameDinamico2')
        self.get_logger().info('FrameDinamico2 iniciado')
        self._broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.5, self.callback)
        self.angle = 0
        
    def callback(self):
        self.angle += math.pi / 30  
        x = math.cos(self.angle)
        y = math.sin(self.angle)

        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "frame_dinamico1" 
        t.child_frame_id = "frame_dinamico2" 
        t.transform.translation.x = x * 2  # Raio da órbita
        t.transform.translation.y = y * 2  # Raio da órbita
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self._broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    frame_dinamico2 = FrameDinamico2()
    rclpy.spin(frame_dinamico2)
    rclpy.shutdown()

if __name__ == '__main__':
    main()