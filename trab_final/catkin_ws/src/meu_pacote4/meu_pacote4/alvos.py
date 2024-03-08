import rclpy
from geometry_msgs.msg import Vector3
from nav_msgs.msg import Odometry

# Callback para a posição do carrinho
def callback_carrinho(msg):
    global posicao_carrinho
    posicao_carrinho = msg.pose.pose.position

# Callback para a posição de cada alvo
def callback_alvo(msg):
    global posicao_carrinho
    global posicao_alvo
    posicao_alvo = msg.pose.pose.position
    # Calcula a diferença entre a posição do carrinho e do alvo
    diferenca_x = posicao_alvo.x - posicao_carrinho.x
    diferenca_y = posicao_alvo.y - posicao_carrinho.y
    # Determina a direção em que o carrinho deve se mover
    if abs(diferenca_x) > abs(diferenca_y):
        # Mover na direção X
        direcao = Vector3()
        direcao.x = 0.1 if diferenca_x > 0 else -0.1
        direcao.y = 0.0
        direcao.z = 0.0
    else:
        # Mover na direção Y
        direcao = Vector3()
        direcao.x = 0.0
        direcao.y = 0.1 if diferenca_y > 0 else -0.1
        direcao.z = 0.0
    # Publica a direção para o tópico de comando do carrinho
    publisher.publish(direcao)

def main():
    global publisher
    global posicao_carrinho
    global posicao_alvo

    rclpy.init()
    node = rclpy.create_node('controlador_carrinho')
    publisher = node.create_publisher(Vector3, '/cmd_vel', 10)

    # Inicializa as posições do carrinho e do alvo
    posicao_carrinho = None
    posicao_alvo = None

    # Inscreve-se nos tópicos de posição do carrinho e de cada alvo
    node.create_subscription(Odometry, '/carrinho/odometry', callback_carrinho, 10)
    node.create_subscription(Odometry, '/alvo1/odometry', callback_alvo, 10)
    node.create_subscription(Odometry, '/alvo2/odometry', callback_alvo, 10)
    node.create_subscription(Odometry, '/alvo3/odometry', callback_alvo, 10)
    node.create_subscription(Odometry, '/alvo4/odometry', callback_alvo, 10)
    node.create_subscription(Odometry, '/alvo5/odometry', callback_alvo, 10)

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()