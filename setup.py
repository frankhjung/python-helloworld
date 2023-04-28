#!/usr/bin/env python
""" Setup. See https://pypi.org/project/setuptools/ """
import setuptools

# pylint: disable=invalid-name
with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-helloworld",
    version="2023.04.28",
    author="Frank Jung",
    author_email="frank.jung@marlo.com.au",
    description="Example hello world project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/theMarloGroup/training/students/fjung/python-helloworld",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL 3",
        "Operating System :: OS Independent",
    ],
)
