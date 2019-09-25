"""CIS189 Python
Author: Greg Tarr
Created: 09/23/2019"""


def average(score1, score2, score3):
    number_tests = 3

    if score1 or score2 or score3 < 0:  # WOAH! Check this out!!
        raise ValueError

    return float((score1 + score2 + score3)/number_tests)


if __name__ == '__main__':

    try:
        average(-10, 12, 14)
    except ValueError as err:
        print("Bad input!")


# Sweet compound relational operators statement!!
