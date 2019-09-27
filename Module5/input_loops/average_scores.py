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
    last_name = input('Please enter your last name: ')
    first_name = input('Please enter your last name: ')
    scores = []
    score = 0
    message = "Please enter a score, or -1 to stop "
    while score != -1:
        score = float(input(message))
        if score == -1:
            break
        scores.append(score)

    avg_scores = average(scores)
    print(last_name + ', ' + first_name + " grade: %5.2f" % avg_scores)


# Run One:
# Please enter your last name: tarr
# Please enter your last name: greg
# Please enter a score, or -1 to stop 33
# Please enter a score, or -1 to stop 44
# Please enter a score, or -1 to stop 55
# Please enter a score, or -1 to stop -1
# tarr, greg grade: 44.00
#
# Process finished with exit code 0

# Run Two:
# Please enter your last name: Tarr
# Please enter your last name: Greg
# Please enter a score, or -1 to stop 33
# Please enter a score, or -1 to stop 5
# Please enter a score, or -1 to stop 1
# Please enter a score, or -1 to stop 0
# Please enter a score, or -1 to stop 99
# Please enter a score, or -1 to stop -1
# Tarr, Greg grade: 27.60
#
# Process finished with exit code 0
