"""CIS189 Python
Author: Greg Tarr
Created: 10/07/2019"""
from fun_with_collections import basic_list_exception


def sort_list(a_list):
    pass


def search_list(a_list, a_value):
    try:
        a_list.index(a_value)
    except ValueError as err:
        return -1
    else:
        return a_list.index(a_value)


if __name__ == '__main__':
    input_value = int(input("Enter an integer to search for: "))
    print(search_list(basic_list_exception.make_list(), input_value))


# I used make_list() here for collecting user input and returning a list.
# As a result of this, a ValueError is returned whenever input is outside the range
# 1-50.  This program does not account for that, and that program does not handle
# the error gracefully.  I avoided making corrections in that file in order to
# ensure that the assignment requirements remained met.
