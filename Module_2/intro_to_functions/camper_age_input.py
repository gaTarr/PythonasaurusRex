"""
Program: camper_age_input.py
Author: Greg Tarr
Last date modified: 09/02/2019

"""

def convert_to_months(months):
    years = months/12
    return years


if __name__ == '__main__':
    age_in_months = input("Enter the camper's age in months:")
    age_in_years = convert_to_months(int(age_in_months))
    print(age_in_years)
