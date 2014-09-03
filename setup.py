#!/usr/bin/python
# -*-coding: utf8-*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
	'mailgun',
	'mailgun.api',
	'mailgun.exceptions',
	'mailgun.parameter',
	'mailgun.utils'
]

setup(
    name="mailgun",
    version="0.0.2",
    author="fatelei",
    author_email="fatelei@gmail.com",
    description="mailgun sdk for python",
    install_requires=["requests", "lepl"],
    packages=packages,
    package_dir={"mailgun": "mailgun"}
)
