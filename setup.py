from setuptools import setup
import os
from glob import glob

package_name = 'teknofest_maden_teknolojileri'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name] if os.path.exists('resource/' + package_name) else []),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'tensorflow', 'numpy', 'opencv-python'],
    zip_safe=True,
    maintainer='Bahattin Yunus',
    maintainer_email='bahattin@example.com',
    description='DeepMine AI: Autonomous Mine Analysis and Agent-Based Planning System',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'reserve_predictor = ai_models.reserve_predictor:main',
            'isg_monitor = sensor_hub.isg_monitor:main',
        ],
    },
)
