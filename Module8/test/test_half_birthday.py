import unittest
from datetime import datetime
from more_fun_with_collections.datetime import half_birthday


class MyTestCase(unittest.TestCase):
    def test_half_birthday_true(self):
        my_last_birthday = datetime(2018, 10, 28)
        self.assertEqual(half_birthday(my_last_birthday), '04/28/19')


if __name__ == '__main__':
    unittest.main()
