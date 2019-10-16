import unittest
from datetime import datetime
from more_fun_with_collections.datetime_assignment import half_birthday


class MyTestCase(unittest.TestCase):
    def test_half_birthday_true(self):
        my_birthday = datetime(2018, 10, 28)
        expected_result = datetime(2019, 4, 28)
        self.assertEqual(half_birthday(my_birthday), expected_result)


if __name__ == '__main__':
    unittest.main()
