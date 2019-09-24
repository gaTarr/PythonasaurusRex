"""CIS189 Python
Author: Greg Tarr
Created: 09/23/2019"""


import unittest
from input_validation import validation_with_if


class MyTestCase(unittest.TestCase):

    def test_input_validation_if(self):
        self.assertEqual(-1, validation_with_if.average(-90, 90, 95))
        self.assertEqual(-1, validation_with_if.average(90, -92, 95))
        self.assertEqual(-1, validation_with_if.average(90, 90, -95))
        self.assertEqual(-1, validation_with_if.average(-90, -90, -95))


if __name__ == '__main__':
    unittest.main()
