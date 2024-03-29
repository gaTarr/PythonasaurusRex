"""CIS189 Python
Author: Greg Tarr
Created: 10/07/2019"""


def make_list():
    number_list = []
    for number in range(3):
        number_input = int(get_input())
        number_list.insert(number, number_input)
    return number_list


def get_input():
    try:
        user_input = int(input("Enter a number: "))
    except ValueError as err:
        raise ValueError
    else:
        return user_input


if __name__ == '__main__':
    print(get_input())
