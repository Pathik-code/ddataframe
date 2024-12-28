import pandas as pd
from faker import Faker
from typing import Dict, Any, Union
from .generators import DataGenerator
from .utils import validate_input, clean_column_spec

class DDataFrame:
    @staticmethod
    def generate(rows: int, columns: Dict[str, Union[str, Dict[str, Any]]]) -> pd.DataFrame:
        """
        Generate a pandas DataFrame with synthetic data.

        Args:
            rows (int): Number of rows to generate
            columns (dict): Column specifications
                          Format: {'column_name': 'faker_provider'} or
                                 {'column_name': {'type': 'faker_provider', **kwargs}}

        Returns:
            pd.DataFrame: Generated DataFrame with synthetic data
        """
        validate_input(rows, columns)
        faker = Faker()
        generator = DataGenerator(faker)
        data = {}

        for col_name, col_spec in columns.items():
            if isinstance(col_spec, str):
                data[col_name] = [getattr(generator, col_spec)() for _ in range(rows)]
            else:
                cleaned_spec = clean_column_spec(col_spec)
                method = cleaned_spec.pop('type')
                data[col_name] = [getattr(generator, method)(**cleaned_spec) for _ in range(rows)]

        return pd.DataFrame(data)
