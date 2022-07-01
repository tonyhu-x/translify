"""Setting up translify using setuptools.

See:
https://github.com/tonyhu-x/translify
https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file.
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    # This determines the name of the project
    name="translify",
    version="0.1.0",
    # This is a one-line description/tagline of what the project does. 
    # This corresponds to the "Summary" metadata field. Check out for more info:
    # https://packaging.python.org/specifications/core-metadata
    description="A tool to translate and summarize a text in a foreign language (not English).",
    # This correspongs to the "Description" metadata field.
    long_description=long_description,
    # This corresponds to the "Description-Content-Type" metadata field.
    long_description_content_type="text/markdown",
    # This corresponds to the "Home-Page" metadata field.
    url="https://github.com/tonyhu-x/translify",
    author="Akshat Naik",
    author_email="akshatn77@gmail.com",
    license="Attribution-NonCommercial-ShareAlike 4.0 International",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: Free for non-commercial use",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(include=["translify"]),
    # Specifies which Python versions are supported. 'pip install' will check this
    # and refuse to install the project if the version does not match.
    python_requires=">=3.8, <4",
    # Specifies what dependencies a project minimally needs to run
    install_requires=[
    	"click>=8.1.3, <9",
        "tensorflow>=2.9.1, <3",
        "torch>=1.11.0, <2",
        "torchaudio>=0.11.0",
        "torchvision>=0.12.0",
        "transformers>=4.19.2, <5",
    ]
)
