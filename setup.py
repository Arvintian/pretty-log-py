# -*- coding:utf-8 -*-

import os
import sys
from distutils.core import setup
from setuptools import find_packages

os.chdir(os.path.dirname(sys.argv[0]) or ".")
here = os.path.abspath(os.path.dirname(__file__))

setup_args = dict(
    name='pretty_logging',
    version='0.0.2',
    description='pretty logging',
    author='v87.us',
    license='WTF',
    url='https://git.v87.us/tianweiguo/pretty-log-py',
    author_email='tianweiguo@renaissance-era.com',
    packages=find_packages(),
    include_package_data=True
)

if 'setuptools' in sys.modules:
    setup_args['zip_safe'] = False
    setup_args['install_requires'] = install_requires = []

    with open('requirements.txt') as f:
        for line in f.readlines():
            req = line.strip()
            if not req or req.startswith('#') or '://' in req:
                continue
            install_requires.append(req)


def main():
    setup(**setup_args)


if __name__ == "__main__":
    main()
