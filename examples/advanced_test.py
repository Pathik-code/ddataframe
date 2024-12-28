import unittest
from ddataframe import DDataFrame

class TestAdvancedDataFrame(unittest.TestCase):
    def setUp(self):
        self.df = DDataFrame()
        self.df.data = {
            'col1': [1, 2, 3],
            'col2': [4, 5, 6]
        }

    def test_add_data(self):
        print("Testing add data...")
        self.df.data['col3'] = [7, 8, 9]
        self.assertTrue('col3' in self.df.data)
        self.assertEqual(self.df.data['col3'], [7, 8, 9])
        print("Add data test passed.")

    def test_remove_data(self):
        print("Testing remove data...")
        del self.df.data['col1']
        self.assertFalse('col1' in self.df.data)
        print("Remove data test passed.")

if __name__ == '__main__':
    unittest.main()
