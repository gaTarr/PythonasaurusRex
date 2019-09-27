import unittest
from input_loops import average_scores


class MyTestCase(unittest.TestCase):
    def test_average(self):
        scores = [3, 5, 7]
        self.assertEqual(5, average_scores.average(scores))


if __name__ == '__main__':
    unittest.main()
