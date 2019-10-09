import unittest

from fun_with_collections import sort_and_search_list


class MyTestCase(unittest.TestCase):
    def test_search_item_found(self):
        self.assertEqual(sort_and_search_list.search_list([8, 11, 5], 11), 1)

    def test_search_item_not_found(self):
        self.assertEqual(sort_and_search_list.search_list([8, 11, 5], 7), -1)


if __name__ == '__main__':
    unittest.main()
