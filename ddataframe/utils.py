from typing import Any, Dict, Union

def validate_input(rows: int, columns: Dict[str, Any]) -> None:
    """
    Validate input parameters for DataFrame generation.

    Args:
        rows (int): Number of rows to generate
        columns (dict): Column specifications

    Raises:
        ValueError: If input parameters are invalid
    """
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Rows must be a positive integer")

    if not isinstance(columns, dict) or not columns:
        raise ValueError("Columns must be a non-empty dictionary")

    for col_name, col_spec in columns.items():
        if not isinstance(col_name, str):
            raise ValueError("Column names must be strings")
        if not isinstance(col_spec, (str, dict)):
            raise ValueError(f"Column specification for {col_name} must be a string or dictionary")

def clean_column_spec(spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Clean and validate column specification.

    Args:
        spec (dict): Column specification

    Returns:
        dict: Cleaned specification
    """
    if 'type' not in spec:
        raise ValueError("Column specification must include 'type' key")

    cleaned_spec = spec.copy()
    # Convert any special method names if needed
    method_mapping = {
        'int': 'random_int',
        'float': 'random_float',
        'element': 'random_element'
    }

    cleaned_spec['type'] = method_mapping.get(cleaned_spec['type'], cleaned_spec['type'])
    return cleaned_spec
