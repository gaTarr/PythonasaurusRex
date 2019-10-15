"""CIS189 Python
Author: Greg Tarr
Created: 10/14/2019"""


def switch_average():
    """ This prompts a user to select from a set of Keys
    and returns the value associated with that key.
    :returns the value of the selected key, or a message
    if an invalid key is selected
    """
    try:
        search_value = input("Choose a Key from (A, B, C, D): ").upper()
    except ValueError:
        print("Invalid Input")
    return {
        'A': 100,
        'B': 200,
        'C': 300,
        'D': 400
    }.get(search_value, 'Invalid Key')


if __name__ == '__main__':
    print(switch_average())
