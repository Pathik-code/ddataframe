from faker import Faker
from typing import Any, List, Union

class DataGenerator:
    def __init__(self, faker: Faker):
        self.faker = faker

    def name(self) -> str:
        return self.faker.name()

    def email(self) -> str:
        return self.faker.email()

    def address(self) -> str:
        """Generate a complete address.
        Returns: str like '123 Main St, City, State'"""
        return self.faker.address()

    def phone_number(self, size: int = 10) -> str:
        return self.faker.numerify('#' * size)

    def date(self, start_date: str = '-30y', end_date: str = 'today') -> str:
        return self.faker.date_between(start_date=start_date, end_date=end_date).isoformat()

    def random_int(self, min: int = 0, max: int = 100) -> int:
        """Generate a random integer between min and max values.
        Args:
            min (int): Minimum value (default: 0)
            max (int): Maximum value (default: 100)
        Example:
            {'type': 'random_int', 'min': 18, 'max': 90}
        Returns: int"""
        return self.faker.random_int(min=min, max=max)

    def random_float(self, min: float = 0, max: float = 100, precision: int = 2) -> float:
        """Generate a random float between min and max values with specified precision.
        Args:
            min (float): Minimum value (default: 0)
            max (float): Maximum value (default: 100)
            precision (int): Number of decimal places (default: 2)
        Example:
            {'type': 'random_float', 'min': 0.0, 'max': 1.0, 'precision': 3}
        Returns: float"""
        return round(self.faker.random.uniform(min, max), precision)

    def random_element(self, elements: List[Any]) -> Any:
        """Select a random element from the provided list.
        Args:
            elements (list): List of elements to choose from
        Example:
            {'type': 'random_element', 'elements': ['HR', 'IT', 'Sales']}
        Returns: Any (type matches input elements)"""
        return self.faker.random_element(elements)

    def number(self, min_value: int = 0, max_value: int = 100) -> int:
        """Generate a random integer.
        Args:
            min_value (int): Minimum value (default: 0)
            max_value (int): Maximum value (default: 100)
        Returns: int"""
        return self.faker.random_int(min=min_value, max=max_value)

    def text(self, max_nb_chars: int = 200) -> str:
        """Generate random text.
        Args:
            max_nb_chars (int): Maximum number of characters (default: 200)
        Returns: str"""
        return self.faker.text(max_nb_chars=max_nb_chars)
