"""CIS189 Python
Author: Greg Tarr
Created: 10/14/2019"""

from datetime import datetime, timedelta


def half_birthday(a_datetime):
    """ This takes a date object and returns a date 6 months later
    :param a_datetime: is the date passed into the function
    ":returns a date 6 months after the date passed in"""
    half_bday = a_datetime + timedelta(days=182)
    print(half_bday)
    return half_bday


if __name__ == '__main__':
    my_last_birthday = datetime(2018, 10, 28)
    print(half_birthday(my_last_birthday))
