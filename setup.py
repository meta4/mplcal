# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='mplcal',
    version='0.1.0',
    description='',
    long_description=readme,
    author='',
    author_email='peter.t.wilson@gmail.com',
    url='https://github.com/meta4/mplcal',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
