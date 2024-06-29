from setuptools import setup, find_packages

setup(
    name="levelaccess",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "geopy",
        "mapillary"
    ],
    author="Dora",
    author_email="doruchan@gmail.com",
    description="A short description of the hackBCN project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/doruchan/hackBCN",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)