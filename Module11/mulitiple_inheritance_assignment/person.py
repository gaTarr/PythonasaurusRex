"""CIS189 Python
Author: Greg Tarr
Created: 10/29/2019"""


class Person:
    """Person class"""

    def __init__(self, lname, fname, addy='', phone=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_characters = set("0123456789 -()")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not (phone_characters.issuperset(phone)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = phone

    def display(self):
        """ This displays variable values from the Person object
        :returns First and last name"""
        return f'{self.last_name}, {self.first_name}'

    def __str__(self):
        return f'{self.last_name}, {self.first_name}\n{self.address}\n{self.phone_number}'

    def __repr__(self):
        return f'{self.last_name}, {self.first_name}\n{self.address}\n{self.phone_number}'


if __name__ == '__main__':
    person1 = Person("Tarr", "Greg", "HOmeor work", "13340400-429")
    print(person1.display_person())
