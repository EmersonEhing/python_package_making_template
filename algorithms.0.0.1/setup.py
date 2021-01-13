import os
import io
import re
from setuptools import find_packages, setup


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(name='algorithms',
      version='0.0.1',
      description='Pythonic Data Structures and Algorithms',
      long_description=long_description(),
      long_description_content_type="text/markdown",
      url='https://github.com/EmersonEhing/python_package_making_template/algorithms.0.0.1',
      author='Algorithms Team & Contributors',
      author_email="halachuinicele@gmail.com",
      license='MIT',
      packages=find_packages(exclude=('tests', 'tests.*')),
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          ],
      zip_safe=False)
