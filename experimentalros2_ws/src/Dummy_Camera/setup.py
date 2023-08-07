from setuptools import setup

package_name = 'Dummy_Camera'

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
            'Dummy_Camera = Dummy_Camera.Dummy_Camera:main',
            'camera_viewer = Dummy_Camera.camera_viewer:main'
        ],
    },
)
