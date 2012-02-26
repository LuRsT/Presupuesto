import os

from setuptools import setup, find_packages


HERE = os.path.abspath(os.path.dirname(__file__))


setup(
    name="presupuesto",
    packages=find_packages(),
    install_requires=["django == 1.3.1"],
    )
