#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

__author__ = 'Takahiro Ikeuchi'

setup(
    name="hipchatpy",
    version="0.0.4",
    packages=['hipchatpy'],
    install_requires=open('requirements.txt').read().splitlines(),
    description="Simple HipChat client library",
    long_description=open('README.txt').read(),
    author='Takahiro Ikeuchi',
    author_email='takahiro.ikeuchi@gmail.com',
    url='https://github.com/iktakahiro/hipchatpy',
    keywords=["HipChat", "HipChat Client"],
    license='MIT',
)

