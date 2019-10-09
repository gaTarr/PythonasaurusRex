import unittest

from fun_with_collections import sort_and_search_list


class MyTestCase(unittest.TestCase):
    def test_search_item_found(self):
        self.assertEqual(sort_and_search_list.search_list([8, 11, 5], 11), 1)

    def test_search_item_not_found(self):
        self.assertEqual(sort_and_search_list.search_list([8, 11, 5], 7), -1)

    def test_sort_list_sorted(self):
        test_input = [8, 11, 5]
        expected_result = [5, 8, 11]
        self.assertEqual(sort_and_search_list.sort_list(test_input), expected_result)


if __name__ == '__main__':
    unittest.main()
