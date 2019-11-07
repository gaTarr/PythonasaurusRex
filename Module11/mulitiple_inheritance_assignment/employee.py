"""CIS189 Python
Author: Greg Tarr
Created: 11/04/2019"""
from datetime import datetime


class Employee():
    """Employee class"""

    # Constructor
    def __init__(self, start_dt, salary):
        # valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ()/'-,")
        # if not (valid_characters.issuperset(start_dt)):
        #     raise ValueError
        # if not isinstance(start_dt, datetime):
        #     raise ValueError("Not a date")
        if not isinstance(salary, int):
            raise AttributeError("Invalid Salary")
        self.start_date = start_dt
        self.salary = salary

    def give_raise(self, more_money):
        """This increases the salary variable the the amount passed in
        :param more_money: this amount is added to the salary variable."""
        self.salary += more_money

    def display(self):
        """ This displays variable values from the Employee object
        :returns Start date and salary."""
        return f"Start Date: {self.start_date} - Salary: ${self.salary:,}"

    def __str__(self):
        return f"Start Date: {self.start_date}\nSalary: ${self.salary:,}\n"

    def __repr__(self):
        return f"Start Date: {self.start_date}\nSalary: ${self.salary:,}\n"


if __name__ == '__main__':
    employee1 = Employee("11/04/2019", 40000)
    print(employee1.display())
    employee1.give_raise(5000)
    print(employee1.display())
    del employee1
