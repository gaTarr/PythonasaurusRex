"""CIS189 Python
Author: Greg Tarr
Created: 09/26/2019"""


def average(score_list):
    counter = 0
    total = 0
    for score in score_list:
        total = total + score
        counter += 1

    return total / counter


if __name__ == '__main__':
    pass
