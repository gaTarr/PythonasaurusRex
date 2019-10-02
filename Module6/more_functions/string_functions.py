"""CIS189 Python
Author: Greg Tarr
Created: 10/01/2019"""


def multiply_string(message, number):
    """ This takes a message and designated number of times the message will be returned/repeated
    :param message: this represents the desired message to be returned
    :param number: this represents the number of times the message will repeat
    :returns: the message a certain number of times.
    """
    result = ''
    for times in range(0, number):
        result = result + message
    return result


if __name__ == '__main__':
    print(multiply_string('test', 6))
