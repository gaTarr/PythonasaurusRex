"""CIS189 Python
Author: Greg Tarr
Created: 10/29/2019"""
from address import Address
from person import Person
from student import Student


if __name__ == '__main__':
    # Driver
    # my_student = Student(900111111, 'Song', 'River')
    # print(my_student.display())
    # my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    # print(my_student.display())
    # my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    # print(my_student.display())
    # del my_student


    # Driver
    addy1 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111')
    person1 = Person('Hammer', 'Martin', addy1)
    print(person1.display_person())
    # apartemnt number is at the end. Why?
    addy2 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111', '16B')
    person2 = Person('Hammer', 'Martin', addy2)
    print(person2.display_person())
    del(addy1, addy2)
    del(person1, person2)
