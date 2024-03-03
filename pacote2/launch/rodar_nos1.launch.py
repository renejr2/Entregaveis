from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Caminho para o arquivo de parâmetros do sistema solar
    params_file_path = os.path.join(
        get_package_share_directory('pacote2'),
        'params',
        'solar_system_params.yaml'
    )

    return LaunchDescription([
        Node(
            package='pacote2',
            executable='frame_fixo',
            name='frame_fixo'
        ),
        Node(
            package='pacote2',
            executable='frame_dinamico1',
            name='frame_dinamico1'
        ),
        Node(
            package='pacote2',
            executable='frame_dinamico2',
            name='frame_dinamico2'
        ),
        Node(
            package='pacote2',
            executable='parameter_reader',
            name='parameter_reader',
            # Passando o caminho do arquivo de parâmetros como argumento
            # para o nó parameter_reader
            arguments=[params_file_path]
        )
    ])