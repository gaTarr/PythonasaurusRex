"""CIS189 Python
Author: Greg Tarr
Created: 09/30/2019"""


def hourly_employee_input():
    """Prompts the user for their name, hours worked, and pay rate, then prints the input"""
    name = input("Please enter your name: ")
    hours_worked = int(input("Enter your hours worked: "))
    hourly_pay_rate = float(input("Enter your hourly pay rate: "))
    print("Name: " + name + ", Hours: " + str(hours_worked) + ", Pay rate: " + str(hourly_pay_rate))


if __name__ == '__main__':
    try:
        hourly_employee_input()
    except ValueError as err:
        print("Invalid Input")



# Trial One:
# # Please enter your name: Greg
# # Enter your hours worked: 40
# # Enter your hourly pay rate: 13.00
# # Name: Greg, Hours: 40, Pay rate: 13.0

# Trial Two:
# Please enter your name: Greg
# Enter your hours worked: -40
# Enter your hourly pay rate: -55.50
# Name: Greg, Hours: -40, Pay rate: -55.5

# Trial Three:
# Please enter your name: Greg
# Enter your hours worked: 4r
# Invalid Input

# The first attempt did not need input validation.  The second trial, needed better input validation than what I used.  It
# allowed the negative input because it's within the rules, but there should be logic to prevent it.  The third trial,
# The input validation worked.
