# Testing Guide

## Setup and Installation

1. Clone and setup environment:
```bash
git clone https://github.com/pathik-code/ddataframe.git
cd ddataframe
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

2. Install test dependencies:
```bash
pip install pytest pytest-cov
```

## Running Tests

### Basic Test Suite
```bash
pytest tests/ --cov=ddataframe
```

### Understanding Test Coverage
The coverage report shows:
- Which parts of code were tested
- Percentage of code coverage
- Untested sections that may need attention

## Interactive Testing

1. Start Python console:
```python
from ddataframe import DDataFrame

# Basic example
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

2. Advanced configuration:
```python
# Complex example with multiple data types
df = DDataFrame.generate(
    rows=10,
    columns={
        'name': 'name',
        'join_date': {'type': 'date', 'start_date': '-5y', 'end_date': 'today'},
        'salary': {'type': 'random_float', 'min': 30000, 'max': 120000, 'precision': 2},
        'department': {'type': 'random_element', 'elements': ['HR', 'IT', 'Sales', 'Marketing']}
    }
)
print(df.head())
print(df.dtypes)  # Check data types
```

## Validation Checks

1. Data Integrity:
   - Verify value ranges (e.g., age between 18-90)
   - Check email format (contains '@')
   - Confirm row count matches input

2. Common Issues:
   - Import errors: Check package installation
   - Test failures: Verify Python version (3.6+)
   - Data issues: Review column specifications
