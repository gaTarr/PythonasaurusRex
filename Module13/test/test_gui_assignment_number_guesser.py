"""CIS189 Python
Author: Greg Tarr
Created: 11/22/2019"""
import unittest
from model.number_guesser import NumberGuesser


class NumberGuesserClassTest(unittest.TestCase):

    def setUp(self):
        self.num_list = [1, 2, 3, 6, 5]
        self.number_guesser = NumberGuesser(self.num_list)

    def tearDown(self):
        del self.number_guesser

    def test_constructor(self):
        self.assertEqual(self.num_list, self.number_guesser.guessed_list)

    def test_number_guesser_str_with_numbers(self):
        expected_result = '1, 2, 3, 6, 5, '
        self.assertEqual(expected_result, self.number_guesser.__str__())

    def test_number_guesser_str_no_numbers(self):
        expected_result = "Empty List"
        self.number_guesser = NumberGuesser()
        self.assertEqual(expected_result, self.number_guesser.__str__())

    def test_add_number(self):
        expected_result = [1, 2, 3, 6, 5, 7]
        expected_input = 7
        self.number_guesser.add_guess(expected_input)
        self.assertEqual(expected_result, self.number_guesser.guessed_list)


if __name__ == '__main__':
    unittest.main()
