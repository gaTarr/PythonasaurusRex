"""CIS189 Python
Author: Greg Tarr
Created: 10/14/2019"""


def score_input(test_name, test_score= '0', invalid_message='Invalid test score, try again!'):
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

    if 0 <= score <= 100:
        return {test_name: test_score}
        # return 'Test name: ' + test_name + ' - ' + str(test_score)
    else:
        return invalid_message


def average_scores(a_dictionary):
    """ This takes a dictionary and returns the average of it's values
    :param a_dictionary: the dictionary of Key:Value pairs
    :returns the average of the values"""
    scores_total = 0
    for test_name, score in a_dictionary.items():
        scores_total += int(score)
    return scores_total / len(a_dictionary)


if __name__ == '__main__':
    try:
        num_scores = int(input("How many test scores? "))
    except ValueError:
        print("Invalid Input")
    scores_dict = dict()
    for scores in range(num_scores):
        scores_dict.update(score_input(input("Enter a test name: ")
                                       , input("Enter a test score between 0 and 100: ")))

    print(scores_dict)
    print("Average Score: " + str(average_scores(scores_dict)))



    # name_input = input("Enter a test name: ")
    # score_num = input("Enter a test score between 0 and 100: ")
    # input_msg = input("Enter Message: ")

    #print(score_input(name_input, score_num, input_msg))
    # print(score_input(name_input, score_num))
