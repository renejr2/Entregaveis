from setuptools import find_packages, setup

package_name = 'pacote2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/rodar_nos1.launch.py']),  # Arquivo de lançamento
        ('share/' + package_name, ['params/solar_system_params.yaml']),  # Arquivo de parâmetros
        ('share/' + package_name + '/srv', ['srv/PlanetParameters.srv']),  # Arquivo de definição do serviço
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='renejunior21@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'frame_fixo = pacote2.frame_fixo:main',  # Adiciona o nó frame_fixo
            'frame_dinamico1 = pacote2.frame_dinamico1:main',  # Adiciona o nó frame_dinamico1
            'frame_dinamico2 = pacote2.frame_dinamico2:main',  # Adiciona o nó frame_dinamico2
            'parameter_reader = pacote2.parameter_reader:main',  # Adiciona o nó parameter_reader
        ],
    },
)