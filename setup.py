from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='csapi',
    version='0.0.1',

    description='A minimalist wrapper around the Apache CloudStack API.',
    long_description=long_description,

    url='https://github.com/swill/csapi',
    author='Will Stevens',
    author_email='wstevens@cloudops.com',
    license='Apache Licence v2.0',

    packages=find_packages(exclude=['docs', 'tests*']),

    install_requires=['requests', 'docopt'],
)
