from setuptools import setup, find_packages

with open('requirements.txt') as f:
    reqs = f.read()

import sys
if sys.version_info < (3,6):
    sys.exit('Sorry, Python < 3.6 is not supported')

setup(
    name='grobid_client',
    version='0.1',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    license='LICENSE.txt',
    long_description=open('Readme.md').read(),
    install_requires=reqs.strip().split('\n'),
)