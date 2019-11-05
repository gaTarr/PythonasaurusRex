"""CIS189 Python
Author: Greg Tarr
Created: 11/04/2019"""
from employee import Employee


class SalariedEmployee(Employee):
    """Salaried Employee class"""

    # Constructor
    def __init__(self, l_name, f_name, st_dt, salary):
        valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ()/'-,")
        if not (valid_characters.issuperset(l_name) and
                valid_characters.issuperset(f_name) and
                valid_characters.issuperset(st_dt)):
            raise ValueError
        if not isinstance(salary, int):
            raise AttributeError("Invalid Salary")
        super().__init__(l_name, f_name)
        self._start_date = st_dt
        self._salary = salary

    def give_raise(self, more_money):
        """This increases the salary variable the the amount passed in
        :param more_money: this amount is added to the salary variable."""
        self._salary += more_money

    def display(self):
        return f"Salaried Employee: {self._first_name} {self._last_name}\n{self._start_date}\n" \
               f"${self._salary:,}\n"


if __name__ == '__main__':
    employee1 = SalariedEmployee("Tarr", "Greg", "11/04/2019", 40000)
    print(employee1.display())
    employee1.give_raise(5000)
    print(employee1.display())
    del employee1
