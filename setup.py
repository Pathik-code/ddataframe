from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ddataframe",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "faker>=8.0.0"
    ],
    author="Pathik Raw Saurav",
    author_email="prsaurav111@gmail.com",
    description="A package for generating synthetic DataFrames with fake data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pathik-code/ddataframe",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'ddataframe=ddataframe.cli:main',
        ],
    },
)
