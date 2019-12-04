"""CIS189 Python
Author: Greg Tarr
Created: 11/30/2019"""
import tkinter as t
from gui_functions import *


def build_gui():
    # Create Dictionary from Text
    create_dictionary_file()

    # Build GUI
    frame = t.Tk()
    frame.title('Anagram Solver')
    frame.geometry('500x210')

    # Display Text
    instructions_text = t.Label(frame, text="Enter an English word to find all anagrams")
    instructions_text.grid(row=2, column=1, columnspan=2, pady=10)
    error_text = t.Label(frame, text='', fg='red')
    error_text.grid(row=4, column=3, padx=7, sticky='W')

    # Buttons
    search_button = t.Button(frame, text='Search', width=20, command=lambda: evaluate_input(word_input_entry.get()))
    search_button.grid(row=4, column=1, padx=10, pady=5)
    reset_button = t.Button(frame, text='Reset', width=20, command=lambda: word_input_entry.delete(0, 'end'))
    reset_button.grid(row=6, column=1, padx=10, pady=5)
    exit_button = t.Button(frame, text='Exit', width=20, command=lambda: frame.destroy())
    exit_button.grid(row=6, column=3, padx=10, pady=5)

    # Input
    word_input_entry = t.Entry(frame, bd=3, justify='center')
    word_input_entry.grid(row=4, column=2, padx=10)

    frame.mainloop()


def display_results_gui(words_list):
    '''This takes a list of words, builds a window, and displays the words line-by-line
    in the window.
    :param words_list: is the list of words to be displayed'''
    results_frame = t.Tk()
    results_frame.title('Anagrams')
    results_frame.geometry('280x210')
    display_row = 2

    # Display Text
    title = t.Label(results_frame, text='All anagrams from your word:')
    title.grid(row=1)

    # Display Results
    for word in words_list:
        display_label = t.Label(results_frame, text=word)
        display_label.grid(row=display_row, padx=25)
        display_row += 1


def display_message(message_text):
    '''This takes a string message, builds a window, and displays the message in the window.
    :param message_text: is the message to be displayed.'''
    message_frame = t.Tk()
    message_frame.title('!')
    message_frame.geometry('200x125')

    # Display Text
    message = t.Label(message_frame, text=message_text)
    message.grid(row=1, pady=50, padx=50)


if __name__ == '__main__':
    build_gui()
