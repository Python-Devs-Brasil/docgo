#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Horacio Ibrahim'
__date__ = '2015-01-25'

''' Setup script for docgo
'''

try:
    from distutils.cor import setup
except ImportError:
    from setuptools import setup

import sys, os
from setuptools import find_packages
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'docgo'))
from docgo.version import __version__

setup(
    name = 'docgo',
    version = __version__,
    author='Horacio Ibrahim',
    author_email = 'horacioibrahim@gmail.com',
    packages=find_packages('docgo'),
    package_dir={'', 'docgo'},
    scripts=[],
    url='https://github.com/horacioibrahim/docgo',
    download_url='https://github.com/horacioibrahim/docgo/releases/tag/0.2', 
    license='MIT License',
    description="This docgo provides a pydoc's tradutor for pt-br",
    long_description = """
    This docgo provides a pydoc's tradutor for pt-br. goslate is an API for
    translate any text using Google Translate. godoc uses this package to
    translate pydoc's .

    See more: goslate for more details.
    """,
    classifiers=[
        'Developement Status :: Production/Stable',
        'Intended Audience :: Dummies Developers',
        'Natural Language :: Brazilian Portuguese',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywors = ['docgo', 'translate', 'pt-br', 'pydoc']
)
