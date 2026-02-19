from setuptools import setup, find_packages
from codecs import open
from os import path

description = 'A minimalist wrapper around the Apache CloudStack API.'
long_description = description

if path.exists('README.md'):
    import shutil
    shutil.copyfile('README.md', 'README.txt')
    # Get the long description from the README file
    with open(path.join(path.abspath(path.dirname(__file__)), 'README.txt'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='csapi',
    version='0.1.0',

    description=description,
    long_description=long_description,

    url='https://github.com/swill/csapi',
    author='Will Stevens',
    author_email='wstevens@cloudops.com',
    license='Apache Licence v2.0',

    packages=find_packages(exclude=['docs', 'tests*']),

    install_requires=['requests', 'docopt'],

    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
