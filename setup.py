#!/usr/bin/env python

import ast
import os
import re
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('stock_algo/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# with open('README.md') as readme_file:
#     README = readme_file.read()

with open("requirements.txt") as reqs:
    REQUIREMENTS = reqs.readlines()

# with open(os.path.join("requirements", "requirements_test.txt")) as reqs:
#     REQUIREMENTS_TEST = reqs.readlines()


setup(
    name='stock_algo',
    version=version,
    description='stock_algo',
    # long_description=README,
    long_description_content_type='text/markdown',
    author='Stock Algo',
    author_email='mla23@njit.edu',
    # url='https://github.com/alpacahq/alpaca-trade-api-python',
    keywords='financial,timeseries,api,trade',
    packages=[
        'stock_algo',
    ],
    install_requires=REQUIREMENTS,
    # tests_require=REQUIREMENTS_TEST,
    setup_requires=['pytest-runner', 'flake8'],
)