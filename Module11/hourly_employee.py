"""CIS189 Python
Author: Greg Tarr
Created: 11/04/2019"""
from employee import Employee


class HourlyEmployee(Employee):
    """Hourly Employee class"""

    # Constructor
    def __init__(self, l_name, f_name, st_dt, h_pay):
        valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ()/'-,")
        if not (valid_characters.issuperset(l_name) and
                valid_characters.issuperset(f_name) and
                valid_characters.issuperset(st_dt)):
            raise ValueError
        if not isinstance(h_pay, float):
            raise AttributeError("Invalid Salary")
        super().__init__(l_name, f_name)
        self._start_date = st_dt
        self._hourly_pay = h_pay

    def give_raise(self, more_money):
        """This accepts an amount and adds it to the hourly_pay variable
        :param more_money: this value is added to the hourly pay"""
        self._hourly_pay += more_money

    def display(self):
        return f"Salaried Employee: {self._first_name} {self._last_name}\n{self._start_date}\n" \
               f"${self._hourly_pay:.2f}\n"


if __name__ == '__main__':
    # Driver
    employee1 = HourlyEmployee("Tarr", "Greg", "11/04/2019", 10.00)
    print(employee1.display())
    employee1.give_raise(2.0)
    print(employee1.display())
    del employee1
