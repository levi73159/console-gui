from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1'
DESCRIPTION = 'GUI for Cosnole'
LONG_DESCRIPTION = 'A package that allows to build simple gui in console'

# Setting up
setup(
    name="console-gui",
    version=VERSION,
    author="Levi",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pynput', 'colorama'],
    keywords=['python', 'console', 'input', 'gui'],
    classifiers=[
        "Development Status :: Planning",
        "Intended Audience :: Python beginners and pros",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
