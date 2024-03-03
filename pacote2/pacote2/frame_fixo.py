import rclpy
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped

class FrameFixo(Node):
    def __init__(self):
        super().__init__('FrameFixo')
        self.get_logger().info('FrameFixo iniciado')
        self._broadcaster = StaticTransformBroadcaster(self)
        
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "world" 
        t.child_frame_id = "frame_fixo" 
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        
        self._broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    frame_fixo = FrameFixo()
    rclpy.spin(frame_fixo)
    rclpy.shutdown()

if __name__ == '__main__':
    main()