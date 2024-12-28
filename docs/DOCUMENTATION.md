# DDataFrame Documentation

## API Reference

### DDataFrame.generate(rows: int, columns: Dict[str, Union[str, Dict[str, Any]]], locale: str = 'en_US') -> pd.DataFrame

Generate synthetic data in a pandas DataFrame format.

#### Parameters:
- `rows`: Number of rows to generate
- `columns`: Column specifications dictionary
  - Simple format: `{'column_name': 'faker_provider'}`
  - Detailed format: `{'column_name': {'type': 'faker_provider', **kwargs}}`

#### Returns:
- `pd.DataFrame`: DataFrame containing the generated synthetic data

#### Example Usage:
```python
from ddataframe import DDataFrame

df = DDataFrame.generate(
    rows=100,
    columns={
        'name': 'name',                     # Simple format
        'age': {                            # Detailed format
            'type': 'random_int',
            'min': 18,
            'max': 90
        },
        'email': 'email',
        'join_date': 'date'
    }
)
```

## Supported Data Types

### Basic Types:
- `name`: Full name
- `first_name`: First name only
- `last_name`: Last name only
- `email`: Email address
- `phone_number`: Phone number
- `date`: Random date
- `random_int`: Integer within range
- `random_float`: Float within range
- `company`: Company name
- `job`: Job title
- `address`: Full address
- `city`: City name
- `country`: Country name

### Advanced Configuration:
```python
# Date ranges
'join_date': {
    'type': 'date',
    'start_date': '-30y',  # 30 years ago
    'end_date': 'today'
}

# Number ranges with distribution
'score': {
    'type': 'random_float',
    'min': 0.0,
    'max': 100.0,
    'precision': 2
}

# Categorical data with weights
'status': {
    'type': 'random_element',
    'elements': ['Active', 'Inactive', 'Pending']
}
