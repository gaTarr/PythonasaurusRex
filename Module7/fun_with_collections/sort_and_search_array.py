"""CIS189 Python
Author: Greg Tarr
Created: 10/09/2019"""
import array as arr

from fun_with_collections import basic_list_exception


def search_array(a_list, a_value):
    """ This takes a list and a value to search for, and if the value is found, returns it's position
    :param a_list: this represents the list which will be searched
    :param a_value: this is the value that will be searched for
    :returns: -1 if the value is not found or the index of the value if it is found
    """
    input_array = arr.array('b', a_list)
    try:
        input_array.index(a_value)
    except ValueError as err:
        return -1
    else:
        return input_array.index(a_value)


def sort_array(a_list):
    """ This takes a list and sorts the values
    :param a_list: this is the list which will be sorted
    :returns: a sorted array of list items
    """
    a_list.sort()
    return arr.array('b', a_list)


if __name__ == '__main__':
    test_list = [10, 33, 2, 4, 22]
    # print(test_list)
    print(sort_array(test_list))
    input_value = int(input("Enter an integer to search for: "))
    print(search_array(basic_list_exception.make_list(), input_value))
