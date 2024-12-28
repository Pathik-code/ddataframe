import unittest
import pandas as pd
from ddataframe import DDataFrame

class TestDDataFrame(unittest.TestCase):
    def test_generate_basic(self):
        df = DDataFrame.generate(
            rows=10,
            columns={
                'name': 'name',
                'email': 'email'
            }
        )
        self.assertEqual(len(df), 10)
        self.assertIn('name', df.columns)
        self.assertIn('email', df.columns)

    def test_generate_with_params(self):
        df = DDataFrame.generate(
            rows=5,
            columns={
                'age': {'type': 'random_int', 'min': 18, 'max': 90},
                'phone': {'type': 'phone_number', 'size': 10}
            }
        )
        self.assertEqual(len(df), 5)
        self.assertTrue(all(18 <= age <= 90 for age in df['age']))
        self.assertTrue(all(len(str(phone)) == 10 for phone in df['phone']))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            DDataFrame.generate(rows=-1, columns={'name': 'name'})

        with self.assertRaises(ValueError):
            DDataFrame.generate(rows=5, columns={})

if __name__ == '__main__':
    unittest.main()
