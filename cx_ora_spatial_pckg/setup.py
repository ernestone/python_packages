#   coding=utf-8
#  #
#   Author: Ernesto Arredondo Martinez (ernestone@gmail.com)
#   File: setup.py
#   Created: 05/04/2020, 00:21
#   Last modified: 05/04/2020, 00:21
#   Copyright (c) 2020
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='cx_oracle_spatial',
    version='0.9',
    packages=find_packages(),
    url='https://github.com/ernestone/python_packages/tree/master/cx_ora_spatial_pckg',
    author='Ernesto Arredondo Martínez',
    author_email='ernestone@gmail.com',
    description='cx_Oracle with spatial capabilities (SDO_GEOM and OGC)',
    long_description=readme(),
    # Ver posibles clasifiers aqui [https://pypi.org/classifiers/]
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'cx_oracle<7',
        'lxml',
        'extra_utils',
        'spatial_utils'
    ],
    python_requires='>=3.7',
    package_data={
        # If any package contains *.txt, *.md or *.yml files, include them:
        "": ["*.txt", "*.md", "*.yml"]
    }
)
