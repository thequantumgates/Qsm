from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='qsm',
    version='0.2.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
