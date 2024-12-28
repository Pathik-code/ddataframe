import unittest
from ddataframe import DDataFrame

class TestBasicDataFrame(unittest.TestCase):
    def setUp(self):
        self.df = DDataFrame()
        self.df.data = {
            'col1': [1, 2],
            'col2': [3, 4]
        }

    def test_data_access(self):
        print("Testing data access...")
        self.assertEqual(self.df.data['col1'], [1, 2])
        self.assertEqual(self.df.data['col2'], [3, 4])
        print("Data access test passed.")

    def test_columns_list(self):
        print("Testing columns list...")
        self.assertEqual(list(self.df.data.keys()), ['col1', 'col2'])
        print("Columns list test passed.")

if __name__ == '__main__':
    unittest.main()
