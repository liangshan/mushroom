# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='mushroom',
    version='0.0.1',
    description='Python RESTful APIs for processing Chinese text',
    author='liangshan',
    url='https://github.com/liangshan/mushroom',
    packages=find_packages(exclude=('test*', )),
    install_requires=[
        'snownlp',
        'flask'
    ],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Programming Language :: Python',

    ],
    package_data={'': ['*.md', '*.txt', '*.marshal', '*.marshal.3']},
    include_package_data=True,
)
