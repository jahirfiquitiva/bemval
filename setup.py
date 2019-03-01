import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="bemval",
    version="0.0.5",
    description="Easily validate emails",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jahirfiquitiva/bemval",
    author="Sebastian Mayorga - Jahir Fiquitiva",
    author_email="hi@jahir.xyz",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["bemval"],
    include_package_data=True
)
