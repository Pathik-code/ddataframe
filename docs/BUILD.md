# Build Guide

## Package Structure
```
ddataframe/
├── ddataframe/
│   ├── __init__.py
│   └── core.py
├── tests/
│   └── test_ddataframe.py
├── docs/
│   ├── DOCUMENTATION.md
│   ├── TESTING.md
│   └── BUILD.md
├── setup.py
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Setup Files

### pyproject.toml
The `pyproject.toml` file is a build system configuration file (PEP 517/518) that:
- Specifies build dependencies before setup.py is processed
- Configures development tools like pytest, black, mypy etc.

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]  # Core build dependencies
build-backend = "setuptools.build_meta"  # Defines the build system to use

[tool.pytest.ini_options]
testpaths = ["tests"]  # Configures pytest to look for tests in tests/ directory
```

Key Benefits:
1. **Standardized Build Process**: Ensures consistent builds across different environments
2. **Isolated Build Dependencies**: Separates build requirements from runtime requirements
3. **Tool Configuration**: Central location for development tool settings
4. **Modern Python Packaging**: Follows current best practices (PEP 517/518)

### setup.py
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ddataframe",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A synthetic data generation tool based on pandas DataFrame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pathik-code/ddataframe",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas>=1.0.0",
        "faker>=8.0.0",
        "numpy>=1.19.0"
    ],
)
```

## Building the Package

1. Install build dependencies:
```bash
pip install build twine
```

2. Build the package:
```bash
python -m build
```

This will create two files in the `dist/` directory:
- A source distribution (.tar.gz)
- A wheel distribution (.whl)

## Testing the Build

1. Create a new virtual environment:
```bash
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate
```

2. Install the built package:
```bash
pip install dist/ddataframe-0.1.0-py3-none-any.whl
```

3. Test the installation:
```python
from ddataframe import DDataFrame
df = DDataFrame.generate(rows=5, columns={'name': 'name'})
print(df)
```

## Publishing (Optional)

1. Test PyPI upload:
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

2. Production PyPI upload:
```bash
twine upload dist/*
```

## Development Installation

For development work, install in editable mode:
```bash
pip install -e .
```
