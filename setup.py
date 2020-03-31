from setuptools import find_packages, setup

from tully import __version__ as version

setup(
    name='tully',
    version=version,
    author="Tully Rankin",
    author_email="tully.rankin@gmail.com",
    url="https://github.com/tullyrankin/tully",
    description="A collection of useful commands to use at the command line.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "tully = tully.cli:main"
        ]
    },
    install_requires=[
        "fire"
    ]
)
