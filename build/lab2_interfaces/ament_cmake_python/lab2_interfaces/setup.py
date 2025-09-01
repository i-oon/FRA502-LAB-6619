from setuptools import find_packages
from setuptools import setup

setup(
    name='lab2_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('lab2_interfaces', 'lab2_interfaces.*')),
)
