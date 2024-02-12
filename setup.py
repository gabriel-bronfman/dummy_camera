from setuptools import setup

package_name = 'dummy_camera_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gabe',
    maintainer_email='gabe@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dummy_camera = src.dummy_camera_node:main',
            'camera_viewer = src.camera_viewer:main'
        ],
    },
)
