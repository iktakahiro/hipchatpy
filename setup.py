#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

__author__ = 'Takahiro Ikeuchi'

setup(
    name="hipchatpy",
    version="0.0.2",
    packages=['hipchatpy'],
    install_requires=open('requirements.txt').read().splitlines(),
    long_description=open('README.txt').read(),
    author='Takahiro Ikeuchi',
    author_email='takahiro.ikeuchi@gmail.com',
    author_twitter='@iktakahiro',
    url='https://github.com/iktakahiro/hipchatpy',
)

