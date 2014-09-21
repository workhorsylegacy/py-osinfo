

import os
from setuptools import setup


readme_content = ""
with open(os.path.join(os.getcwd(), 'README.rst'), 'r') as f:
    readme_content = f.read()

setup(
    name = "py-osinfo",
    version = "0.1.1",
    author = "Matthew Brennan Jones",
    author_email = "matthew.brennan.jones@gmail.com",
    description = 
"A module for getting the OS type, brand, release, and kernel with Python 2 & 3",
    long_description=readme_content,
    license = "MIT",
    url = "https://github.com/workhorsy/py-osinfo",
    packages=['osinfo'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)

