import unittest
from more_functions import validate_input_in_functions as viif


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(viif.score_input('Exam 1'), "Test name: Exam 1 - 0")

        with self.assertRaises(TypeError):
            viif.score_input()

    def test_score_input_test_score_valid(self):
        self.assertEqual(viif.score_input('Good', 77), "Test name: Good - 77")

    def test_score_input_test_score_below_range(self):
        self.assertEqual(viif.score_input('Below', -1), "Invalid test score, try again!")

    def test_score_input_test_score_above_range(self):
        self.assertEqual(viif.score_input('Above', 101), "Invalid test score, try again!")

    def test_test_score_non_numeric(self):
        self.assertEqual(viif.score_input('Above', 'Sixty'), "Invalid test score, try again!")

    def test_score_input_invalid_message(self):
        self.assertEqual(viif.score_input('Above', 101, 'WRONG!!'), "WRONG!!")


if __name__ == '__main__':
    unittest.main()
