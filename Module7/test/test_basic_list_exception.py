import unittest
from unittest.mock import patch

from fun_with_collections import basic_list_exception


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='8')
    def test_make_list(self, input):
        self.assertEqual(basic_list_exception.make_list(), [8, 8, 8])

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='-1')
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='51')
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()


if __name__ == '__main__':
    unittest.main()
