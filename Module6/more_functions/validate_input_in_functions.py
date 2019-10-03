"""CIS189 Python
Author: Greg Tarr
Created: 10/01/2019"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """ This takes a test name, score, and error message, validates the input, and returns a message
    :param test_name: this represents the test name
    :param test_score: this represents the test score
    :param invalid_message: this is the message returned when an invalid score is returned
    :returns: the invalid_message param if test_score param is not within desired value.
    """
    try:
        score = float(test_score)
    except ValueError:
        return invalid_message

    if 0 <= test_score <= 100:
        return 'Test name: ' + test_name + ' - ' + str(test_score)
    else:
        return invalid_message


if __name__ == '__main__':
    name_input = input("Enter a test name: ")
    score_num = float(input("Enter a test score between 0 and 100: "))
    input_msg = input("Enter Message: ")

    #print(score_input(name_input, score_num, input_msg))
    print(score_input(name_input, score_num))
