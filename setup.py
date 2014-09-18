
# FIXME: change so we don't need package and module name:
# from src import osinfo

import os
from setuptools import setup

setup(
    name = "py-osinfo",
    version = "0.1.0",
    author = "Matthew Brennan Jones",
    author_email = "matthew.brennan.jones@gmail.com",
    description = 
"A module for getting the OS type, brand, release, and kernel with Python 2 & 3",
    long_description=
'''
Py-osinfo should work without any extra programs or libraries, beyond
 what your OS provides. The goal is for this to work on every OS that
 Python supports. Works on Linux, OS X, Windows, BSD, Solaris, 
Cygwin, and Haiku.
''',
    license = "MIT",
    url = "https://github.com/workhorsy/py-osinfo",
    packages=['src'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)

