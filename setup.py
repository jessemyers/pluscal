#!/usr/bin/env python
from setuptools import find_packages, setup


project = "pluscal"
version = "0.1.0"


setup(
    name=project,
    version=version,
    description="PlusCal AST and builder in Python",
    author="Jesse Myers",
    url="https://github.com/jessemyers/pluscal",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    keywords="PlusCal",
    install_requires=[
    ],
    extras_require=dict(
        dist=[
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
            "nose>=1.3.7",
            "PyHamcrest>=1.9.0",
        ],
        typehinting=[
            "mypy>=0.670.0",
        ],
    ),
)
