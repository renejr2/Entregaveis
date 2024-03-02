import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.get_logger().info('Sensor Subscriber iniciado')
        
        self.velocidade_subscriber = self.create_subscription(Twist, 'velocidade_sensor', self.callback, 10)
        self.velocidade_modulo_publisher = self.create_publisher(Float32, 'velocidade_modulo', 10)
    
    def callback(self, msg):
        self.get_logger().info('Callback chamada')
        
        linear = msg.linear
        angular = msg.angular
        modulo = (linear.x**2 + linear.y**2 + linear.z**2 +
                  angular.x**2 + angular.y**2 + angular.z**2)**0.5

        self.get_logger().info('Módulo dos vetores: {}'.format(modulo))

        # Criar mensagem Float32
        msg_modulo = Float32()
        msg_modulo.data = modulo

        # Publicar mensagem
        self.velocidade_modulo_publisher.publish(msg_modulo)

def main(args=None):
    rclpy.init(args=args)
    sensor_subscriber = SensorSubscriber()
    rclpy.spin(sensor_subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()