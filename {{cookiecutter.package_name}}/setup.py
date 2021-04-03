"""Setup Package Module"""

from setuptools import find_packages, setup

setup(
    name="{{cookiecutter.package_name}}",
    version="0.1.0",
    url="{{cookiecutter.author_url}}",
    license="MIT",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    description="{{cookiecutter.package_desc}}",
    packages=find_packages(exclude="src.tests")
)
