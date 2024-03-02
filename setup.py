from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="strip-notebook-metadata",  # this is the package name with hyphens
    version="0.1.1",
    author="Kyriaki Mavropoulou",
    author_email="kyriaki@quanterra.gr",
    description="A package to strip metadata from code cells and markdowns without editing the output in Jupyter notebooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kyriaki-mvr/strip-notebook-metadata",
    packages=find_packages(),
    install_requires=[
        "nbformat>=5.0.0",
    ],
    entry_points={
        'console_scripts': [
            'strip-notebook-metadata=strip_notebook_metadata.main:strip_metadata',
        ],
    },
    license="GPL"
)
