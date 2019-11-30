"""CIS189 Python
Author: Greg Tarr
Created: 11/19/2019"""
import tkinter as t
import tkinter
import tkinter.messagebox
from model.number_guesser import NumberGuesser

# Global Variable to hold NumberGuesser object
numbers = None


def play_game():
    """This activates all the buttons in the GUI, creates a NumberGuesser object"""
    for button in button_list:
        button.config(state='normal')
    global numbers
    numbers = NumberGuesser()


def evaluate_button(selection, button):
    """This takes a number and the button that was clicked. It adds the number to the list in the
    NumberGuesser object, and deactivates the button that was clicked.
    :param selection is the number passed in by the button click
    :param button is the button that was clicked"""
    if selection == numbers.get_random_number():
        winner()
    elif selection in numbers.guessed_list:
        display_message.config(text="Number already guessed")
    else:
        numbers.add_guess(selection)
        button.config(state='disabled')
        display_message.config(text=f'Guesses: {numbers}')


def winner():
    """This displays a messagebox with a win-message. Then, it calls a method to reset the game."""
    tkinter.messagebox.showinfo("Success", "WINNER!!!")
    reset()


def reset():
    """This resets the display of the list of numbers, clears the list of numbers in the NumberGuesser
    object, and resets the random number generated in the NumberGuesser object.  It also deactivates
    all the buttons in the GUI"""
    display_message.config(text=' ')
    numbers.guessed_list.clear()
    numbers.random_number = None
    for button in button_list:
        button.config(state='disabled')


# Create GUI
landing_window = t.Tk()
landing_window.title('Random Number Game')
landing_window.geometry('400x400')

# Label for instructions
instructions = t.Label(landing_window, text="Press start, then guess the number..")
instructions.grid(row=1, column=1)

# Label to display guessed numbers
display_message = t.Label(landing_window, text=" ")
display_message.grid(row=8, column=2)

# Button to start game
start_button = t.Button(landing_window, text='Start', width=20, command=play_game)
start_button.grid(row=2, column=1, pady=4)

# Prepare number buttons
button_one = t.Button(landing_window, text='1', command=lambda: evaluate_button(1, button_one))
button_one.grid(row=4, column=1, pady=1)
button_one.config(state='disabled')
button_two = t.Button(landing_window, text='2', command=lambda: evaluate_button(2, button_two))
button_two.grid(row=5, column=1, pady=1)
button_two.config(state='disabled')
button_three = t.Button(landing_window, text='3', command=lambda: evaluate_button(3, button_three))
button_three.grid(row=6, column=1, pady=1)
button_three.config(state='disabled')
button_four = t.Button(landing_window, text='4', command=lambda: evaluate_button(4, button_four))
button_four.grid(row=7, column=1, pady=1)
button_four.config(state='disabled')
button_five = t.Button(landing_window, text='5', command=lambda: evaluate_button(5, button_five))
button_five.grid(row=8, column=1, pady=1)
button_five.config(state='disabled')
button_six = t.Button(landing_window, text='6', command=lambda: evaluate_button(6, button_six))
button_six.grid(row=9, column=1, pady=1)
button_six.config(state='disabled')
button_seven = t.Button(landing_window, text='7', command=lambda: evaluate_button(7, button_seven))
button_seven.grid(row=10, column=1, pady=1)
button_seven.config(state='disabled')
button_eight = t.Button(landing_window, text='8', command=lambda: evaluate_button(8, button_eight))
button_eight.grid(row=11, column=1, pady=1)
button_eight.config(state='disabled')
button_nine = t.Button(landing_window, text='9', command=lambda: evaluate_button(9, button_nine))
button_nine.grid(row=12, column=1, pady=1)
button_nine.config(state='disabled')
button_ten = t.Button(landing_window, text='10', command=lambda: evaluate_button(10, button_ten))
button_ten.grid(row=13, column=1, pady=1)
button_ten.config(state='disabled')

# Add all buttons to a list
button_list = [button_one, button_two, button_three, button_four, button_five, button_six, button_seven, button_eight,
               button_nine, button_ten]

# Button to reset the game
reset_button = t.Button(landing_window, text='Reset', width=20, command=reset)
reset_button.grid(row=15, column=1, pady=4)

landing_window.mainloop()

if __name__ == '__main__':
    num_list = [1, 2, 3, 6, 5]
    num_list2 = []
    test_guesser = NumberGuesser(num_list)
    test_guesser2 = NumberGuesser(num_list2)
    print(test_guesser)
    print(test_guesser2)
    test_guesser.add_guess(9)
    print(test_guesser)
    print(test_guesser.get_random_number())
