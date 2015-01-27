#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Horacio Ibrahim'
__date__ = '2015-01-25'

''' Setup script for docgo
'''

try:
    from distutils.core import setup
except ImportError:
    from setuptools import setup

#import sys, os
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'docgo'))

setup(
    name = 'docgo',
    version = '0.5',
    author='Horacio Ibrahim',
    author_email = 'horacioibrahim@gmail.com',
    packages=['docgo'],
    url='https://github.com/horacioibrahim/docgo',
    download_url='https://github.com/horacioibrahim/docgo/tarball/master',
    license='MIT License',
    description="docgo is a pydoc's translator",
    install_requires=['goslate>=1.3.0'],
    long_description = """
    This docgo provides a pydoc's tradutor. The goslate is an API for \n
    translate any text using Google Translate. The docgo use it for \n
    translate pydoc's.
    """,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords = ['docgo', 'translate', 'pydoc'],
)
