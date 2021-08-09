from setuptools import setup
from setuptools import find_packages

setup(
   name='pywhy_sample',
   version='1.0',
   description='pywhy-sample installation test',
   packages=find_packages(exclude=["*.tests"]),
   # the list of runtime dependencies required by this built package
   install_requires=[
   ],
   author='why',
   author_email='wh.y@navercorp.com',
   python_requires='>3.6'
)