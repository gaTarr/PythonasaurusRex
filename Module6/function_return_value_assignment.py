"""CIS189 Python
Author: Greg Tarr
Created: 09/30/2019"""


def hourly_employee_input():
    """Prompts the user for their name, hours worked, and pay rate, then prints the input"""
    name = input("Please enter your name: ")
    try:
        hours_worked = int(input("Enter your hours worked: "))
    except ValueError as err:
        raise ValueError
    else:
        try:
            hourly_pay_rate = float(input("Enter your hourly pay rate: "))
        except ValueError as err:
            raise ValueError
        else:
            weekly_pay(hours_worked,hourly_pay_rate)
            return "Name: " + name + ", Weekly Pay: " + str(weekly_pay(hours_worked,hourly_pay_rate))


def weekly_pay(hours_worked, hourly_pay_rate):
    """Calculates Weekly pay from parameters"""
    return hours_worked * hourly_pay_rate


if __name__ == '__main__':
    try:
        display_string = hourly_employee_input()
    except ValueError as err:
        print("Invalid Input")
    else:
        print(display_string)



