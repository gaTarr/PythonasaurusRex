import unittest
from more_fun_with_collections import dict_membership as dm


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        test_dictionary = {'AAA':100, 'AA':95, 'A':90, 'B':80, 'C':70}
        test_value = 'B'
        self.assertTrue(dm.in_dict(test_dictionary, test_value))

    def test_in_dict_false(self):
        test_dictionary = {'AAA':100, 'AA':95, 'A':90, 'B':80, 'C':70}
        test_value = 'BB'
        self.assertFalse(dm.in_dict(test_dictionary, test_value))


if __name__ == '__main__':
    unittest.main()
