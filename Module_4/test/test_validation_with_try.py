"""CIS189 Python
Author: Greg Tarr
Created: 09/23/2019"""

import unittest
from input_validation import validation_with_try as valid_try


class MyTestCase(unittest.TestCase):
    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            valid_try.average(90, - 89, 78)


if __name__ == '__main__':
    unittest.main()
