
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="proto-schema-tests",
    version="0.1.0",
    author="Vagelis Ladas",
    author_email="el159@le.ac.uk",
    description="Base for tests of Protobuf schemas",
    url="https://github.com/vl62/proto-schema-tests.git",
    license="Apache 2",
    packages=['tests'],
    classifiers=[
        "License :: OSI Approved :: Apache 2 License",
    ]
)