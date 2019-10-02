import unittest
from source_file import average_lists


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # This is how we initialize for each test
        test_list = [3, 4, 6, 8, 12, 19, 72]

    def tearDown(self):
        test_list = []

    def test_list(self):
        self.assertAlmostEqual(average_lists.average([3, 4, 6, 8, 12, 19, 72], 17.7142857)) #This doesn't work yet..


if __name__ == '__main__':
    unittest.main()
