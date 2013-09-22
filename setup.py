#!/usr/bin/env python

import os
import sys

import binaryornot

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='binaryornot',
    version='0.2.0',
    description='Ultra-lightweight pure Python package to check if a file is binary or text.',
    long_description=readme + '\n\n' + history,
    author='Audrey Roy',
    author_email='audreyr@gmail.com',
    url='https://github.com/audreyr/binaryornot',
    packages=[
        'binaryornot',
    ],
    package_dir={'binaryornot': 'binaryornot'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='binaryornot',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
