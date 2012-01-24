import os

from setuptools import setup, find_packages


HERE = os.path.abspath(os.path.dirname(__file__))


setup(
    name="presupuesto",
    packages=find_packages(),
    install_requires=["django == 1.3.1"],
    entry_points="""
        # -*- Entry points: -*-
        [console_scripts]
        manage = presupuesto.manage:main

        """,
    )
