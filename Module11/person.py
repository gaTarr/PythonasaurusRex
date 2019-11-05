"""CIS189 Python
Author: Greg Tarr
Created: 10/29/2019"""


class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy


    def display_person(self):
        return f'{self.last_name}, {self.first_name}\n{self.address.display()}'

