import rclpy
from rclpy.node import Node
from pacote2 import PlanetParameters
import yaml

class ParameterReader(Node):
    def __init__(self):
        super().__init__('parameter_reader')
        self.get_logger().info('ParameterReader inicializado')

        self.declare_parameters(
            namespace='',
            parameters=[
                ('file_path', None)
            ]
        )

        file_path = self.get_parameter('file_path').get_parameter_value().string_value
        with open(file_path, 'r') as file:
            self.params = yaml.safe_load(file)['solar_system_params']

        self.service = self.create_service(
            PlanetParameters,
            'get_planet_parameters',
            self.get_planet_parameters_callback
        )

    def get_planet_parameters_callback(self, request, response):
        if request.planet_name in self.params:
            response.orbit_radius = self.params[request.planet_name]['orbit_radius']
            response.success = True
            response.message = f"Parâmetros para {request.planet_name} obtidos com sucesso."
        else:
            response.success = False
            response.message = f"Parâmetros para {request.planet_name} não encontrados."
        return response

def main(args=None):
    rclpy.init(args=args)
    parameter_reader = ParameterReader()
    rclpy.spin(parameter_reader)
    rclpy.shutdown()

if __name__ == '__main__':
    main()