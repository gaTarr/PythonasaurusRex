"""CIS189 Python
Author: Greg Tarr
Created: 11/30/2019"""
import unittest

from model.anagram import Anagram


class AnagramClassTest(unittest.TestCase):
    def setUp(self):
        self.word_no_anagrams = 'baseball'
        self.word_with_anagrams = 'spear'
        self.word_with_symbols = 'wor%'
        self.word_with_numbers = 'wor3'
        self.word_with_caps = 'Words'
        self.word_with_no_caps = 'words'
        self.anagram = Anagram(self.word_no_anagrams)

    def tearDown(self):
        del self.anagram

    def test_constructor_with_word_with_symbols(self):
        with self.assertRaises(ValueError):
            self.anagram = Anagram(self.word_with_symbols)

    def test_constructor_with_word_with_numbers(self):
        with self.assertRaises(ValueError):
            self.anagram = Anagram(self.word_with_numbers)

    def test_constructor_with_word_with_caps(self):
        expected_result = 'dorsw'
        expected_anagram = Anagram(self.word_with_caps)
        self.assertEqual(expected_anagram.get_sorted_anagram(), expected_result)


if __name__ == '__main__':
    unittest.main()
