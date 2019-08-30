import imp
import os
from setuptools import setup, find_packages

version = imp.load_source(
    'dbloy.version', os.path.join('dbloy', 'version.py')).version

setup(
    name='dbloy',
    version=version,
    description='Continuous Delivery tool for PySpark Notebooks based jobs on Databricks.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=['PyYAML>=5.1.2',
                      'databricks-cli>=0.8.7'
                      ],
    entry_points='''
        [console_scripts]
        dbloy=dbloy.cli:cli
    ''',
    author='Hjörtur Hjartarson',
    author_email='hjorturh88@gmail.com',
    maintainer='Hjörtur Hjartarson',
    maintainer_email='hjorturh88@gmail.com',
    url='https://github.com/hjh17/dbloy',
    packages=find_packages(exclude=['tests', 'tests.*']),
    license=['MIT'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='databricks cli ci/cd'
)