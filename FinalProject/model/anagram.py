"""CIS189 Python
Author: Greg Tarr
Created: 11/30/2019"""


class Anagram:

    def __init__(self, word):
        '''Constructor'''
        # Verify input is alpha characters
        allowed_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
        if not (allowed_characters.issuperset(word)):
            raise ValueError
        self.word = word
        self.sorted_anagram = self.order_letters()

    def order_letters(self):
        '''This takes the word class member, strips white space, converts to lowercase, and
        alphabetizes the letters. Then, it returns the result.
        :return sorted result of letters.'''
        word_lower = self.word.strip().lower()
        alphabetized_letters = sorted(list(word_lower))
        return "".join(alphabetized_letters)

    def get_sorted_anagram(self):
        '''This returns the sorted anagram member of the class.
        :return sorted anagram.'''
        return self.sorted_anagram

    def __str__(self):
        return f'Word: {self.word} - Sorted Anagram: {self.sorted_anagram}'


