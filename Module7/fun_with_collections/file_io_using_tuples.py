"""CIS189 Python
Author: Greg Tarr
Created: 10/09/2019"""
import os


def write_to_file(a_tup):
    """This accepts information, opens a file, and adds to the file,
    then closes the file
    :param a_tup: this is the information to be added to the file
    """
    try:
        file = open('student_info.txt', 'a')
        try:
            file.write(str(a_tup) + "\n")
        finally:
            file.close()
    except IOError:
        print("File Error in Write..")


def get_student_info(student_name='No name entered'):
    """this prompts a user for scores, then passes the username and scores
    to the write_to_file() method
    ":param student_name: this keyword argument is the name of the student
    """
    scores_list = []
    not_done = True
    while not_done:
        try:
            score = float(input("Enter a score, or -1 to quit: "))
            if score < -1:
                raise ValueError
        except ValueError:
            print("Invalid input!")
        else:
            if score == -1:
                not_done = False
            else:
                scores_list.append(score)
    return_tuple = student_name, scores_list
    write_to_file(return_tuple)


def read_from_file():
    """This opens a file, reads the contents, then closes the file
    """
    try:
        file_dir = os.path.dirname(__file__)
        file_name = "student_info.txt"
        file = open(os.path.join(file_dir, file_name), "r")
        try:
            for lines in file:
                print(lines)
        finally:
            file.close()
    except IOError:
        print("File Error in Read..")


if __name__ == '__main__':
    get_student_info(student_name='Greg')
    get_student_info(student_name='Jamie')
    get_student_info(student_name='Michelle')
    get_student_info(student_name='Amy')
    read_from_file()
