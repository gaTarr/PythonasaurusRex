"""CIS189 Python
Author: Greg Tarr
Created: 10/14/2019"""


def in_set(a_set, a_value):
    """ This accepts a set and a value to examine
    :param a_set: is the set that's passed in
    :param a_value: is the value is going to be tested for in the set
    :returns True if the value is in the set, False if the value is not in the set"""
    return a_value in a_set


if __name__ == '__main__':
    our_set = {1, 2, 3}
    our_value = 3

    print(in_set(our_set, our_value))
