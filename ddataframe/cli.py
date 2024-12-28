import argparse
import json
from typing import Dict
from .core import DDataFrame
from .generators import DataGenerator
from faker import Faker

DATA_TYPE_HELP: Dict[str, str] = {
    'name': 'Generates a full name (e.g., "John Doe")',
    'email': 'Generates an email address (e.g., "john.doe@example.com")',
    'address': 'Generates a complete address (e.g., "123 Main St, City, State")',
    'phone_number': 'Generates a phone number (e.g., "555-123-4567")',
    'date': '''Generates a date in ISO format. Options:
        Format: {'type': 'date', 'start_date': '-30y', 'end_date': 'today'}
        start_date: Start date (default: '-30y')
        end_date: End date (default: 'today')''',
    'number': '''Generates a random integer. Options:
        Format: {'type': 'number', 'min_value': 0, 'max_value': 100}
        min_value: Minimum value (default: 0)
        max_value: Maximum value (default: 100)''',
    'text': '''Generates random text. Options:
        Format: {'type': 'text', 'max_nb_chars': 200}
        max_nb_chars: Maximum number of characters (default: 200)''',
    'random_int': '''Generates a random integer between min and max values.
        Format: {'type': 'random_int', 'min': 18, 'max': 90}
        min: Minimum value (default: 0)
        max: Maximum value (default: 100)
        Example: Will generate numbers like 18, 45, 72, 90''',

    'random_float': '''Generates a random float with specified precision.
        Format: {'type': 'random_float', 'min': 0.0, 'max': 1.0, 'precision': 3}
        min: Minimum value (default: 0.0)
        max: Maximum value (default: 100.0)
        precision: Number of decimal places (default: 2)
        Example: Will generate numbers like 0.756, 0.234, 0.999''',

    'random_element': '''Selects a random element from a provided list.
        Format: {'type': 'random_element', 'elements': ['HR', 'IT', 'Sales']}
        elements: List of possible values to choose from
        Example: Will randomly select one value from the provided list'''
}

def show_help():
    print("DDataFrame - Synthetic Data Generator")
    print("\nAvailable Data Types and Formats:")
    print("==================================")

    # Group data types by category
    categories = {
        "Basic Types": ['name', 'email', 'address', 'phone_number'],
        "Numeric Types": ['random_int', 'random_float', 'number'],
        "Date and Time": ['date'],
        "Selection Types": ['random_element'],
        "Text Types": ['text']
    }

    for category, types in categories.items():
        print(f"\n{category}:")
        for dtype in types:
            if dtype in DATA_TYPE_HELP:
                print(f"\n{dtype}:")
                print(f"    {DATA_TYPE_HELP[dtype]}")

    print("\nUsage Examples:")
    print('''
    Simple format:
        {'column_name': 'data_type'}

    Extended format with options:
        {'column_name': {'type': 'data_type', **options}}

    Example:
        {
            'name': 'name',
            'birth_date': {'type': 'date', 'start_date': '-30y', 'end_date': 'today'},
            'score': {'type': 'number', 'min_value': 0, 'max_value': 100}
        }
    ''')

def show_datatypes():
    """Display core datatypes and their descriptions"""
    print("\nAvailable Data Types:")
    print("===================")

    # Group data types by category
    categories = {
        "Basic Types": ['name', 'email', 'address', 'phone_number'],
        "Numeric Types": ['random_int', 'random_float', 'number'],
        "Date and Time": ['date'],
        "Selection Types": ['random_element'],
        "Text Types": ['text']
    }

    for category, types in categories.items():
        print(f"\n{category}:")
        for dtype in types:
            if dtype in DATA_TYPE_HELP:
                print(f"\n{dtype}:")
                print(f"    {DATA_TYPE_HELP[dtype]}")

def show_all_providers():
    """Display all available providers including Faker methods"""
    print("\nAll Available Data Providers:")
    print("==========================")

    # Show core types first
    print("\nCore Data Types:")
    show_datatypes()

    # Show additional Faker providers
    print("\nAdditional Faker Providers:")
    print("(These require the extended format with 'type' specified)")

    faker = Faker()
    generator = DataGenerator(faker)
    methods = [method for method in dir(generator)
              if not method.startswith('_') and
                 callable(getattr(generator, method)) and
                 method not in DATA_TYPE_HELP]

    for method in sorted(methods):
        doc = getattr(generator, method).__doc__ or "No description available"
        print(f"\n{method}:")
        print(f"    Description: {doc}")
        print(f"    Usage: {{'type': '{method}'}}")

def show_errors():
    """Display common errors and their solutions"""
    print("\nCommon Errors and Solutions:")
    print("===========================")

    errors = {
        "Invalid JSON format": {
            "Example": 'ddataframe --rows 10 --columns {name: name}',
            "Solution": 'Use proper JSON format with quotes:\n        ddataframe --rows 10 --columns \'{"name": "name"}\''
        },
        "Unknown data type": {
            "Example": '--columns \'{"name": "invalid_type"}\'',
            "Solution": "Use --types to see available data types"
        },
        "Invalid parameters": {
            "Example": '--columns \'{"age": {"type": "random_int"}}\'',
            "Solution": "Specify required parameters (e.g., min and max for random_int)"
        }
    }

    for error, details in errors.items():
        print(f"\n{error}:")
        print(f"    Example: {details['Example']}")
        print(f"    Solution: {details['Solution']}")

def show_examples():
    """Display usage examples for different commands"""
    print("\nCommand Line Usage Examples:")
    print("==========================")

    examples = {
        "Basic CSV Generation": {
            "command": "ddataframe --rows 100 --columns '{\"name\": \"name\", \"email\": \"email\"}' --output data.csv",
            "description": "Generates a CSV file with names and emails"
        },
        "JSON Output": {
            "command": "ddataframe --rows 50 --columns '{\"age\": {\"type\": \"random_int\", \"min\": 18, \"max\": 90}}' --format json --output data.json",
            "description": "Generates a JSON file with age data"
        },
        "Complex Example": {
            "command": '''ddataframe --rows 200 --columns '{
    "name": "name",
    "join_date": {"type": "date", "start_date": "-5y", "end_date": "today"},
    "department": {"type": "random_element", "elements": ["HR", "IT", "Sales"]}
}' --output employees.csv''',
            "description": "Generates employee data with multiple columns and types"
        }
    }

    for title, info in examples.items():
        print(f"\n{title}:")
        print(f"Description: {info['description']}")
        print(f"Command: {info['command']}")

def parse_columns(columns_str):
    """Parse and validate JSON column specifications"""
    try:
        return json.loads(columns_str)
    except json.JSONDecodeError:
        raise ValueError(
            "Invalid JSON format in columns argument.\n"
            "Example: '{\"name\": \"name\", \"age\": {\"type\": \"random_int\", \"min\": 18, \"max\": 90}}'"
        )

def main():
    parser = argparse.ArgumentParser(
        description='DDataFrame - Synthetic DataFrame Generator',
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Create argument groups
    required_args = parser.add_argument_group('required generation arguments')
    required_args.add_argument('--rows', type=int, help='Number of rows to generate')
    required_args.add_argument('--columns', type=str, help='Column specifications in JSON format')

    # Optional arguments
    parser.add_argument('--output', type=str, default='output.csv',
                       metavar='FILE',
                       help='Output file path (default: output.csv)')
    parser.add_argument('--format', choices=['csv', 'json'],
                       default='csv',
                       metavar='FORMAT',
                       help='Output format: csv or json (default: csv)')
    parser.add_argument('--types', action='store_true',
                       help='Show available data types and their formats')
    parser.add_argument('--examples', action='store_true',
                       help='Show command usage examples')
    parser.add_argument('--list-types', action='store_true',
                       help='List all available data types including Faker providers')
    parser.add_argument('--errors', action='store_true',
                       help='Show common errors and their solutions')
    parser.add_argument('--all-providers', action='store_true',
                       help='Show all available data providers including additional Faker methods')

    args = parser.parse_args()

    # Handle help commands first
    if args.types:
        show_help()
        return

    if args.examples:
        show_examples()
        return

    if args.list_types:
        show_datatypes()
        return

    if args.all_providers:
        show_all_providers()
        return

    if args.errors:
        show_errors()
        return

    # Validate required arguments
    if not args.rows or not args.columns:
        parser.error("--rows and --columns are required when not using --types")

    try:
        # Generate data
        columns = parse_columns(args.columns)
        df = DDataFrame.generate(rows=args.rows, columns=columns)

        # Save output
        if args.format == 'csv':
            df.to_csv(args.output, index=False)
        else:
            df.to_json(args.output, orient='records')

        print(f"Generated data saved to {args.output}")

    except ValueError as e:
        print(f"Error: {str(e)}")
        print("Use --errors to see common errors and solutions")
        exit(1)
    except Exception as e:
        print(f"Error: Unexpected error occurred: {str(e)}")
        print("Use --errors to see common errors and solutions")
        exit(1)

if __name__ == '__main__':
    main()
