#!/usr/bin/python
#-*-coding: utf8-*-

from setuptools import setup

setup(
    name="mailgun",
    version="0.0.2",
    author="fatelei",
    author_email="fatelei@gmail.com",
    description="mailgun sdk for python",
    install_requires=["requests", "lepl"],
    packages=["mailgun"],
    package_dir={".": "mailgun"}
)
