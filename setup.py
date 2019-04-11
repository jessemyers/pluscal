#!/usr/bin/env python
from setuptools import find_packages, setup


project = "pluscal"
version = "0.3.0"


url = "https://github.com/jessemyers/pluscal"
long_description = f"See {url}"
try:
    with open("README.md") as file_:
        long_description = file_.read()
except IOError:
    pass


setup(
    name=project,
    version=version,
    license="Apache 2.0",
    description="PlusCal AST and builder in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jesse Myers",
    url=url,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    keywords="PlusCal TLA+",
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
    ],
    extras_require=dict(
        dist=[
            "bumpversion>=0.5.3",
            "pip>=19.0.3",
            "setuptools>=40.8.0",
            "twine>=1.13.0",
        ],
        lint=[
            "flake8>=3.7.7",
            "flake8-isort>=2.7.0",
            "flake8-print>=3.1.0",
        ],
        test=[
            "coverage>=4.5.3",
            "nose>=1.3.7",
            "PyHamcrest>=1.9.0",
        ],
        typehinting=[
            "mypy>=0.670.0",
        ],
    ),
)
