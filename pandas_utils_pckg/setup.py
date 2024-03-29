#   coding=utf-8
#  #
#   Author: Ernesto Arredondo Martinez (ernestone@gmail.com)
#   File: setup.py
#   Created: 05/04/2020, 00:21
#   Last modified: 05/04/2020, 00:21
#   Copyright (c) 2020
from setuptools import setup, find_packages
import os

GIT_REPO = os.getenv('GIT_REPO', 'https://github.com/ernestone/python_packages')


def format_requirement(n_pckg):
    str_req = f'{n_pckg} @ git+{GIT_REPO}#egg={n_pckg}&subdirectory={n_pckg}_pckg'

    path_dev = os.getenv('PATH_DEVELOPER_MODE')
    if path_dev and os.path.exists(path_dev):
        str_req = f'{n_pckg} @ ' \
                  f'file://{os.path.join(path_dev, "{}_pckg".format(n_pckg))}' \
                  f'#egg={n_pckg}'

    print(str_req)
    return str_req


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='pandas_utils',
    version='0.9',
    packages=find_packages(),
    url=f'{GIT_REPO}/tree/master/pandas_utils_pckg',
    author='Ernesto Arredondo Martínez',
    author_email='ernestone@gmail.com',
    description='Pandas and geopandas utils',
    long_description=readme(),
    # Ver posibles clasifiers aqui [https://pypi.org/classifiers/]
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'geopandas',
        format_requirement('cx_oracle_spatial')
    ],
    python_requires='>=3.6',
    package_data={
        # If any package contains *.txt, *.md or *.yml files, include them:
        "": ["*.txt", "*.md", "*.yml"]
    }
)
