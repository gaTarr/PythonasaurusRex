"""CIS189 Python
Author: Greg Tarr
Created: 11/30/2019"""
from gui_functions import *
import pickle

# master_file = open("source/words_alpha.txt", "r")
# anagram_dictionary = {}
# # print(master_file.read())
#
# for line in master_file.readlines():
#     alphabetized_letters = format_input(line)
#     word_input = line.strip().lower()
#     # print(f'{line.strip()}: {alphabetized_letters} - {len(line.strip())}')
#
#     if alphabetized_letters in anagram_dictionary:
#         anagram_dictionary[alphabetized_letters].append(word_input)
#     else:
#         anagram_dictionary[alphabetized_letters] = [word_input]
#
# with open('/Users/grego/git/Python/PythonasaurusRex/FinalProject/source/anagramdict.obj', 'wb') as dictionary_file:
#     pickle.dump(anagram_dictionary, dictionary_file, -1)
#     dictionary_file.close()

# ///////////////////////////////////////////////////////////////Open/extract


# with open('source/anagramdict.obj', 'rb') as search_file:
#     working_dict = pickle.load(search_file)
#     search_file.close()
#     print(working_dict)
#     words_list = working_dict.get('aeprs')
#     for word in words_list:
#         print(word)
