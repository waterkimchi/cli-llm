from setuptools import setup

setup(
    name="clillm",
    version="0.1.0",
    packages=["clillm"],
    entry_points={"console_scripts": ["clillm = clillm.main:main"]},
)
