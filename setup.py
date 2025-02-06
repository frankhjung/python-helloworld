#!/usr/bin/env python
"""Setup. See https://pypi.org/project/setuptools/"""

import setuptools

# pylint: disable=invalid-name
with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-helloworld",
    version="2023.08.21",
    author="Frank Jung",
    author_email="frank.jung@liux.com",
    description="Example hello world project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/frankhjung1/python-helloworld",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL 3",
        "Operating System :: OS Independent",
    ],
)
