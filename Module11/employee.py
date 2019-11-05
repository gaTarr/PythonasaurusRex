"""CIS189 Python
Author: Greg Tarr
Created: 11/04/2019"""


class Employee:
    """Employee Class"""

    # Constructor
    def __init__(self, l_name, f_name, addr=' ', phone=' '):
        self._last_name = l_name
        self._first_name = f_name
        self._address = addr
        self._phone_number = phone

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def set_last_name(self, l_name):
        self._last_name = l_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def set_first_name(self, f_name):
        self._first_name = f_name

    @property
    def address(self):
        return self._address

    @address.setter
    def set_address(self, addr):
        self._address = addr

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def set_phone_number(self, phone):
        self._phone_number = phone

    def display(self):
        return f"{self._first_name} {self._last_name}\n{self._address}\n{self._phone_number}\n"
