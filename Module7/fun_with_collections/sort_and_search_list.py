"""CIS189 Python
Author: Greg Tarr
Created: 10/07/2019"""
from fun_with_collections import basic_list_exception


def sort_list(a_list):
    """ This takes a list and sorts the values
    :param a_list: this is the list which will be sorted
    :returns: the list after it has been sorted"""
    a_list.sort()
    return a_list


def search_list(a_list, a_value):
    """ This takes a list and a value to search for, and if the value is found, returns it position
    :param a_list: this represents the list which will be searched
    :param a_value: this is the value that will be searched for
    :returns: -1 if the value is not found or the index of the value if it is found
    """
    try:
        a_list.index(a_value)
    except ValueError as err:
        return -1                       # return was included here to gracefully handle value not found
    else:
        return a_list.index(a_value)    # return to show user where value is


if __name__ == '__main__':
    test_list = [10, 33, 2, 4, 22]
    # print(test_list)
    print(sort_list(test_list))
    input_value = int(input("Enter an integer to search for: "))
    print(search_list(basic_list_exception.make_list(), input_value))


# I used make_list() here for collecting user input and returning a list.
# As a result of this, a ValueError is returned whenever input is outside the range
# 1-50.  This program does not account for that, and that program does not handle
# the error gracefully.  I avoided making corrections in that file in order to
# ensure that the assignment requirements remained met.
