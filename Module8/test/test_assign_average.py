import unittest
from unittest import mock

from more_fun_with_collections.assign_average import switch_average


class MyTestCase(unittest.TestCase):
    def test_found_a(self):
        with mock.patch('builtins.input', side_effect=['A']):
            assert switch_average() == 100

    def test_found_b(self):
        with mock.patch('builtins.input', side_effect=['B']):
            assert switch_average() == 200

    def test_found_c(self):
        with mock.patch('builtins.input', side_effect=['C']):
            assert switch_average() == 300

    def test_found_d(self):
        with mock.patch('builtins.input', side_effect=['D']):
            assert switch_average() == 400

    def test_found_e(self):
        with mock.patch('builtins.input', side_effect=['E']):
            assert switch_average() == 'Invalid Key'


if __name__ == '__main__':
    unittest.main()
