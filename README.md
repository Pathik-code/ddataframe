# DDataFrame

A Python package for generating synthetic DataFrames with fake data for testing and development purposes.

## Documentation

Complete documentation is available in our docs folder:

- [Main Documentation](docs/DOCUMENTATION.md) - Full API reference and supported data types
- [Examples](docs/EXAMPLES.md) - Code examples and use cases
- [Testing Guide](docs/TESTING.md) - Installation and testing instructions
- [Build Guide](docs/BUILD.md) - Package building and distribution

## Installation

```bash
pip install ddataframe
```

## Features

- Generate pandas DataFrames with synthetic data
- Support for various data types including:
  - Names (first name, last name, full name)
  - Email addresses
  - Phone numbers with customizable formats
  - Dates
  - Addresses
  - Numbers (int, float)
  - And all other Faker providers

## Quick Start

### Setup Environment

```bash
git clone https://github.com/pathik-code/ddataframe.git
cd ddataframe
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

### Basic Usage

```python
from ddataframe import DDataFrame

df = DDataFrame.generate(
    rows=5,
    columns={
        'name': 'name',
        'email': 'email',
        'age': {'type': 'random_int', 'min': 18, 'max': 90}
    }
)
print(df)
```

## Command Line Interface

Generate synthetic data directly from the command line:

```bash
# Show available data types
ddataframe --types

# Generate CSV file
ddataframe --rows 1000 --columns '{"name": "name", "email": "email"}' --output data.csv

# Generate JSON file with complex types
ddataframe --rows 500 --columns '{
    "name": "name",
    "birth_date": {"type": "date", "start_date": "-30y", "end_date": "today"},
    "department": {"type": "random_element", "elements": ["HR", "IT", "Sales"]}
}' --format json --output data.json
```

### CLI Options

- `--rows`: Number of rows to generate (required)
- `--columns`: Column specifications in JSON format (required)
- `--output`: Output file path (default: output.csv)
- `--format`: Output format (csv or json, default: csv)
- `--types`: Show available data types
- `--all-providers`: Show all available providers
- `--errors`: Show common errors and solutions
- `--list-types`: List core data types

## Supported Data Types

### Basic Types
- `name`: Full name generation
- `email`: Email address
- `address`: Complete address
- `phone_number`: Phone number with custom format

### Numeric Types
- `random_int`: Integer with range
- `random_float`: Float with precision
- `number`: Simple number generation

### Date and Time
- `date`: Date with customizable range

### Selection Types
- `random_element`: Choose from list of options

### Text Types
- `text`: Random text generation

## Project Structure

```
ddataframe/
│
├── ddataframe/
│   ├── __init__.py
│   ├── core.py
│   ├── generators.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   └── test_ddataframe.py
│
├── README.md
├── setup.py
├── requirements.txt
└── LICENSE
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
