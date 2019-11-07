"""CIS189 Python
Author: Greg Tarr
Created: 11/04/2019"""
from datetime import datetime, date

from mulitiple_inheritance_assignment.employee import Employee
from person import Person


class Manager(Employee, Person):
    """Manager class"""

    # Constructor
    def __init__(self, l_name, f_name, start_dt, salary, dept='', reports_list=[]):
        Employee.__init__(self, start_dt, salary)
        Person.__init__(self, l_name, f_name)
        self.department = dept
        self.direct_reports_list = reports_list

    def give_raise(self, more_money):
        """ This overrides a method in a parent class, which increases the value of a variable
        :param more_money: this represents the value that will be added to the 'salary' variable"""
        self.salary += more_money

    def display_direct_reports(self, reports_list):
        """ This returns a formatted string of employee objects by calling an inherited method of the
        parent class.
        :param reports_list: this is the list of employees
        :returns a string of employee objects"""
        reports = ''
        for r in reports_list:
            reports += '\n\t' + r.display()
        return reports

    def display(self):
        """ This displays variable values from the manager object by calling inherited methods
        :returns First and last name, start date and salary, and direct report employees"""
        return f'{Person.display(self)}: {Employee.display(self)}\nDirect Reports:' \
               f'{self.display_direct_reports(reports_list)}'


if __name__ == '__main__':
    employee1 = Employee(date(2019, 10, 20), 33000)
    employee2 = Employee(date(2004, 9, 4), 39000)
    employee3 = Employee(date(1985, 2, 3), 303000)
    reports_list = [employee1, employee2, employee3]
    manager1 = Manager("Tarr", "Greg", datetime(2019, 5, 20), 40000, "Human Resources", reports_list)
    print(manager1.display()) # This the display call calls display methods from both parent classes and the manager class
    manager1.give_raise(2000)
    print(manager1.display())  # This the display call calls display methods from both parent classes and the manager class
    del employee1, employee2, employee3, manager1



