#!/usr/bin/env python

import sys, os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

version = '0.4.3'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

setup(
    name='binaryornot',
    version=version,
    description=(
        'Ultra-lightweight pure Python package to check '
        'if a file is binary or text.'
    ),
    long_description=readme + '\n\n' + history,
    author='Audrey Roy Greenfeld',
    author_email='aroy@alum.mit.edu',
    url='https://github.com/audreyr/binaryornot',
    packages=[
        'binaryornot',
    ],
    package_dir={'binaryornot': 'binaryornot'},
    include_package_data=True,
    install_requires=[
        'chardet>=3.0.2',
    ],
    license="BSD",
    zip_safe=False,
    keywords='binaryornot',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
)
