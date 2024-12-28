# DDataFrame Documentation

## API Reference

### DDataFrame.generate(rows: int, columns: Dict[str, Union[str, Dict[str, Any]]]) -> pd.DataFrame

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

### Advanced Configuration:
```python
# Date ranges
'join_date': {
    'type': 'date',
    'start_date': '-30y',  # 30 years ago
    'end_date': 'today'    # Current date
}

# Number ranges
'score': {
    'type': 'random_float',
    'min': 0.0,
    'max': 100.0,
    'precision': 2
}
