import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-example-fjung",
    version="0.1.0",
    author="Frank Jung",
    author_email="frank.jung@marlo.com.au",
    description="Example hello world project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/theMarloGroup/training/students/fjung/python-example",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL 3",
        "Operating System :: OS Independent",
    ]
)
