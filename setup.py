# -*- coding: utf-8 -*-

from setuptools import setup
from os.path import abspath, dirname, join

path = abspath(dirname(__file__))

classifiers = (
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: MIT License',
)

required = (
    'pandas'
)

kw = {
    'name': 'vincent',
    'version': '0.1.0',
    'description': 'A Python to Vega translator',
    'long_description': open(join(path, 'README.md')).read(),
    'author': 'Rob Story',
    'author_email': 'wrobstory@gmail.com',
    'license': 'MIT License',
    'url': 'https://github.com/wrobstory/vincent',
    'keywords': 'data visualization',
    'classifiers': classifiers,
    'py_modules': ['vincent'],
    'install_requires': required,
    'zip_safe': True,
}

setup(**kw)