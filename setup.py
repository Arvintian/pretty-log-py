#!/usr/bin/python
# -*- coding:utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

setup_args = dict(
    name='pretty_logging',
    version='0.0.1',
    description='pretty logging',
    author='v87.us',
    license='WTF',
    url='https://git.v87.us/tianweiguo/pretty-log-py',
    author_email='tianweiguo@renaissance-era.com',
    packages=find_packages(),
    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    install_requires=[]
)

def main():
    setup(**setup_args)

if __name__ == "__main__":
    main()