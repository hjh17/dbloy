#!/usr/bin/env python
from setuptools import setup

with open("my_python_lib/_version.py") as version_file:
    exec(version_file.read())


setup(
    name='my_python_lib',
    version=__version__,
    description='A PySpark logic extracted into a python library',
    author='Hjörtur Hjartarson',
    author_email='hjorturh88@gmail.com',
    packages=["my_python_lib"]
)
