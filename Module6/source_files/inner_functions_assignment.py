"""CIS189 Python
Author: Greg Tarr
Created: 10/02/2019"""


def measurements(a_list):
    """ This takes a list of measurements, performs some calculations, then returns the results in a string
    :param a_list: this is a list of one or two measurement inputs
    :returns: a string containing perimeter and area values based on inputs
    """
    def area(b_list):
        """ This takes a list of measurements, and determines the area
        :param b_list: this represents the list of measurements
        :returns: depending whether one or two measurements input, area is returned
        """
        if len(b_list) == 1:
            return b_list[0] * b_list[0]
        else:
            return a_list[0] * a_list[1]

    def perimeter(c_list):
        """ This takes a list of measurements, and determines the perimeter
        :param c_list: this represents a list of measurements
        :returns: depending whether one or two measurements input, perimeter is returned
        """
        if len(c_list) == 1:
            return c_list[0] * 4
        else:
            return (c_list[0] + c_list[1]) * 2

    return "Perimeter = " + str(perimeter(a_list)) + " Area = " + str(area(a_list))
