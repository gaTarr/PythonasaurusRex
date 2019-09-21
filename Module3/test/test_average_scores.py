"""CIS189 Python
Author: Greg Tarr
Created: 09/02/2019"""


import unittest
import unittest.mock as mock
from format_output import average_scores


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85,90,95]):
            assert average_scores.average() == 90


if __name__ == '__main__':
    unittest.main()


#Test 1 failed because the average() function had not been written yet

#Test 2 passed because the average() function had been written, and
#the logic of the function correctly calculated average.

