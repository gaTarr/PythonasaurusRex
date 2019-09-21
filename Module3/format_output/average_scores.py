"""CIS189 Python
Author: Greg Tarr
Created: 09/02/2019"""


def average():
    score_one = float(input("Enter first score: "))
    score_two = float(input("Enter second score: "))
    score_three = float(input("Enter third score: "))
    return (score_one + score_two + score_three) / 3


if __name__ == '__main__':
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first Name: ")
    age = int(input("Enter your age: "))
    average_scores = average()

    print(last_name + ", " + first_name + " age: " + str(age) + " average grade: %5.2f" % average_scores)



