from setuptools import setup, find_packages

setup(
    name="strip-notebook-metadata",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "nbformat>=5.0.0",
    ],
    entry_points={
        'console_scripts': [
            'strip-notebook-metadata=strip_notebook_metadata.main:strip_metadata',
        ],
    },
    author="Kyriaki Mavropoulou",
    author_email="kyriaki@quanterra.gr",
    description="A utility to strip metadata from code and markdown cells in Jupyter notebooks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="GPL",
    url="https://github.com/kyriaki-mvr/strip-notebook-metadata",
)

