import unittest
from more_fun_with_collections import set_membership as sm


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        test_set = set('12345')
        test_value = 4
        self.assertTrue(sm.in_set(test_set, test_value))

    def test_in_set_false(self):
        test_set = set('12345')
        test_value = 7
        self.assertFalse(sm.in_set(test_set, test_value))


if __name__ == '__main__':
    unittest.main()
