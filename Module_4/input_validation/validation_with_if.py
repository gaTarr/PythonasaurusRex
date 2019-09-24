"""CIS189 Python
Author: Greg Tarr
Created: 09/23/2019"""


def average(score1, score2, score3):
    number_tests = 3
    if score1 < 0 or score2 < 0 or score3 < 0:
        return -1
    else:
        return float((score1 + score2 + score3)/number_tests)


if __name__ == '__main__':
    pass
