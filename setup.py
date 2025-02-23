from setuptools import setup

setup(
    name="clillm",
    version="0.1.0",
    packages=["clillm"],
    install_requires=[
        "typer",
        "colorama",
        "shellingham",
        "pytest",
    ],
    entry_points={"console_scripts": ["clillm = clillm.__main__:main"]},
)
