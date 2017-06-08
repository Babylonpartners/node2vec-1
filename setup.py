#!/usr/bin/env python
import os

from distutils.core import setup
from setuptools import find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as fh:
    install_requires = fh.read().splitlines()

with open('VERSION') as fh:
    version = fh.read().strip()

setup(
    name='node2vec',
    version=version,
    description='Adapting the word2vec model to graphs.',
    author='Babylon Health',
    packages=find_packages(exclude=('test',)),
    zip_safe=True,
    include_package_data=False,
    license='Proprietary',
    long_description=(
        'https://github.com/Babylonpartners/node2vec-core'
    ),
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP'
    ],
    entry_points={
        'console_scripts': [
            'node2vec = node2vec:main'
        ]
    },
    # package_data={
    #     'spacy_interface.config': ['config.ini.dist']
    # },
)
