"""CIS189 Python
Author: Greg Tarr
Created: 11/16/2019"""
import re


class Customer:
    """Customer Class"""

    # Constructor
    def __init__(self, cust_id, l_name, f_name, phone_n):
        phone_format = "\w{3}-\w{3}-\w{4}"
        if (not isinstance(cust_id, int)) or (not 1000 <= cust_id <= 9999):
            raise InvalidCustomerIdException
        if (not l_name.isalpha()) or (not f_name.isalpha()):
            raise InvalidNameException
        if not re.search(phone_format, phone_n):
            raise InvalidPhoneNumberFormat
        self.customer_id = cust_id
        self.last_name = l_name
        self.first_name = f_name
        self.phone_number = phone_n

    def __str__(self):
        return f"Customer Id: {self.customer_id}, Last: {self.last_name}, First: " \
               f"{self.first_name}, Phone: {self.phone_number}"

    def __repr__(self):
        return f"Customer Id: {self.customer_id}, Last: {self.last_name}, First: " \
               f"{self.first_name}, Phone: {self.phone_number}"

    def display(self):
        """This displays class members just like the str method
        :returns a display string"""
        return f"{self.first_name} {self.last_name} ({self.customer_id}) " \
               f"Phone: {self.phone_number}"


class InvalidCustomerIdException(Exception):
    pass


class InvalidNameException(Exception):
    pass


class InvalidPhoneNumberFormat(Exception):
    pass


if __name__ == '__main__':
    # Driver
    test_customer = Customer(5556, "Tarr", "Greg", "515-123-4567")
    try:
        id_customer = Customer(55566, "Tarr", "Greg", "515-123-4567")
    except InvalidCustomerIdException:
        print("Invalid Customer Id")
    try:
        lname_customer = Customer(5556, "T4rr", "Greg", "515-123-4567")
    except InvalidNameException:
        print("Invalid Customer Name")
    try:
        fname_customer = Customer(5556, "Tarr", "Gre8", "515-123-4567")
    except InvalidNameException:
        print("Invalid Customer Name")
    try:
        phone_customer = Customer(5556, "Tarr", "Greg", "515123-4567")
    except InvalidPhoneNumberFormat:
        print("Invalid Customer Phone Number")
    try:
        print(test_customer.__str__())
    except TypeError:
        print("Error")

