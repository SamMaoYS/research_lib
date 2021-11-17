#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name="research_lib",
    version="1.0",
    author="Yongsen Mao",
    url="https://github.com/SamMaoYS/research_lib.git",
    description="Library for Research Scripts",
    packages=find_packages(exclude=("configs", "tests")),

    include_package_data=True,
    install_requires=["configparser==5.0.2", "hydra-core==1.1.1", "matplotlib==3.3.4", "numpy==1.19.5",
                      "omegaconf==2.1.1", "opencv-python==4.5.1.48", "Pillow==8.2.0", "progress==1.6", 
                      "protobuf==3.13.0", "psutil==5.8.0", "pymeshlab==0.2.1", "pyrender==0.1.45",
                      "pytimeparse==1.1.8", "scipy==1.5.4", "requests==2.22.0", "trimesh==3.9.16"]
)