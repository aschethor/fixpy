from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.6'
DESCRIPTION = 'Simple event-driven programming'
LONG_DESCRIPTION = 'A package that facilitates event-driven programming in python'

# Setting up
setup(
    name="fixpy",
    version=VERSION,
    author="Nils Wandel",
    author_email="<wandeln@cs.uni-bonn.de>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    project_urls={
        'Source Code': 'https://github.com/aschethor/fixpy',
    },
    packages=find_packages(),
    install_requires=['matplotlib', 'numpy', 'networkx'],
    keywords=['python', 'event', 'events', 'event-driven', 'fixed-point iteration'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
