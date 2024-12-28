# DDataFrame Examples

## Basic Usage Examples

### 1. Simple Person Data
```python
from ddataframe import DDataFrame

# Generate basic personal information
df = DDataFrame.generate(
    rows=5,
    columns={
        'name': 'name',
        'email': 'email',
        'age': {'type': 'random_int', 'min': 18, 'max': 65}
    }
)
print(df)
```

### 2. Employee Database
```python
# Create employee dataset with various data types
employees = DDataFrame.generate(
    rows=10,
    columns={
        'employee_id': {'type': 'random_int', 'min': 1000, 'max': 9999},
        'name': 'name',
        'department': {
            'type': 'random_element',
            'elements': ['HR', 'IT', 'Sales', 'Marketing']
        },
        'salary': {
            'type': 'random_float',
            'min': 35000,
            'max': 120000,
            'precision': 2
        },
        'join_date': {
            'type': 'date',
            'start_date': '-3y',
            'end_date': 'today'
        }
    }
)
print(employees.head())
print("\nData Types:")
print(employees.dtypes)
```

### 3. International Customer Data
```python
# Generate customer data with different locales
german_customers = DDataFrame.generate(
    rows=3,
    columns={
        'name': 'name',
        'address': 'address',
        'phone': 'phone_number'
    }
)

french_customers = DDataFrame.generate(
    rows=3,
    columns={
        'name': 'name',
        'address': 'address',
        'phone': 'phone_number'
    }
)

print("German Customers:")
print(german_customers)
print("\nFrench Customers:")
print(french_customers)
```

### 4. E-commerce Orders
```python
# Generate synthetic e-commerce order data
orders = DDataFrame.generate(
    rows=5,
    columns={
        'order_id': {'type': 'random_int', 'min': 10000, 'max': 99999},
        'customer_name': 'name',
        'product': {
            'type': 'random_element',
            'elements': ['Laptop', 'Phone', 'Tablet', 'Headphones']
        },
        'quantity': {'type': 'random_int', 'min': 1, 'max': 5},
        'price': {'type': 'random_float', 'min': 99.99, 'max': 2499.99, 'precision': 2},
        'order_date': {'type': 'date', 'start_date': '-30d', 'end_date': 'today'},
        'status': {
            'type': 'random_element',
            'elements': ['Pending', 'Shipped', 'Delivered']
        }
    }
)

print("E-commerce Orders:")
print(orders)
print("\nOrder Statistics:")
print(f"Total Orders: {len(orders)}")
print(f"Average Price: ${orders['price'].mean():.2f}")
```

### 5. Data Analysis Example
```python
# Generate and analyze student data
import pandas as pd

students = DDataFrame.generate(
    rows=100,
    columns={
        'student_id': {'type': 'random_int', 'min': 1000, 'max': 9999},
        'name': 'name',
        'grade': {'type': 'random_float', 'min': 60, 'max': 100, 'precision': 1},
        'subject': {
            'type': 'random_element',
            'elements': ['Math', 'Science', 'English', 'History']
        }
    }
)

# Analyze the data
print("Student Grade Analysis:")
print("\nAverage Grade by Subject:")
print(students.groupby('subject')['grade'].agg(['mean', 'min', 'max']))

# Plot grade distribution (requires matplotlib)
try:
    students['grade'].hist(bins=20, title='Grade Distribution')
except ImportError:
    print("Install matplotlib for visualization capabilities")
```

## Working with Generated Data

### Export to Different Formats
```python
# Generate sample data
df = DDataFrame.generate(
    rows=10,
    columns={'name': 'name', 'email': 'email'}
)

# Export to CSV
df.to_csv('sample_data.csv', index=False)

# Export to Excel
df.to_excel('sample_data.xlsx', index=False)

# Export to JSON
df.to_json('sample_data.json', orient='records')
```

These examples demonstrate various use cases for generating synthetic data with DDataFrame. You can customize the data generation based on your specific needs by adjusting the parameters and combining different data types.
