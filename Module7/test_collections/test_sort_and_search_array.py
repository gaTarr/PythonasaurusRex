import unittest
from fun_with_collections import sort_and_search_array as ssa


class MyTestCase(unittest.TestCase):
    def test_search_item_found(self):
        test_input = [8, 11, 5]
        test_case = 11
        expected_result = 1
        self.assertEqual(ssa.search_array(test_input, test_case), expected_result)

    def test_search_item_not_found(self):
        test_input = [8, 11, 5]
        test_case = 7
        expected_result = -1
        self.assertEqual(ssa.search_array(test_input, test_case), expected_result)

    def test_sort_list_sorted(self):
        test_input = [8, 11, 5]
        expected_result = [5, 8, 11]
        self.assertEqual(ssa.sort_array(test_input), expected_result)


if __name__ == '__main__':
    unittest.main()
