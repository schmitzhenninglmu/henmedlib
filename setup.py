__author__ = "Henning Schmitz"

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="henmedlib",
    version="0.0.4",
    author="Henning Schmitz",
    author_email="H.Schmitz@physik.uni-muenchen.de ",
    description="Package encapsulating all functions I used during my PhD.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schmitzhenninglmu/henmedlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
