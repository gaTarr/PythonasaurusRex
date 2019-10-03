"""CIS189 Python
Author: Greg Tarr
Created: 10/02/2019"""


def measurements(a_list):
    def area(b_list):
        return a_list[0] * a_list[1]

    def perimeter(c_list):
        return (a_list[0] + a_list[1]) * 2

    return "Perimeter = " + str(perimeter(a_list)) + " Area = " + str(area(a_list))
