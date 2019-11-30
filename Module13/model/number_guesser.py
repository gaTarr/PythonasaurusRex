"""CIS189 Python
Author: Greg Tarr
Created: 11/22/2019"""
import random


class NumberGuesser:

    def __init__(self, guesses=[]):
        self.guessed_list = guesses
        self.random_number = random.randint(1, 10)

    def get_random_number(self):
        return self.random_number

    def __str__(self):
        guessed_numbers = ''
        if not self.guessed_list:
            return "Empty List"
        else:
            for nums in self.guessed_list:
                guessed_numbers += f'{nums}, '
            return guessed_numbers

    def add_guess(self, num):
        self.guessed_list.append(num)
