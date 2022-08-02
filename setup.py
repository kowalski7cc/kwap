#!/usr/bin/env python3

from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='kwap',
    version='0.1',
    description='Work with Karaf Web API',
    url='#',
    requires=['requests', 'urllib3'],
    author='kowalski7cc',
    license='MIT',
    packages=['kwap'],
    entry_points={
        'console_scripts': [
            'kwap = kwap.__main__:main'
        ]
    },
    zip_safe=True
)
