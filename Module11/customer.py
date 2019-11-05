"""CIS189 Python
Author: Greg Tarr
Created: 11/04/2019"""


class Customer:
    """Customer Class"""

    # Constructor
    def __init__(self, cust_id, l_name, f_name, phone_n, addr):
        if not isinstance(cust_id, int):
            raise AttributeError("'Customer' object has no attribute 'cid'")
        valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()'-, ")
        if not (valid_characters.issuperset(l_name) and
                valid_characters.issuperset(f_name) and
                valid_characters.issuperset(addr) and
                valid_characters.issuperset(phone_n)):
            raise ValueError
        self.customer_id = cust_id
        self.last_name = l_name
        self.first_name = f_name
        self.phone_number = phone_n
        self.address = addr

    def __str__(self):
        return f"Customer Id: {self.customer_id}, Last: {self.last_name}, First: " \
               f"{self.first_name}, Phone: {self.phone_number}, Address: {self.address}"

    def __repr__(self):
        return f"Customer Id: {self.customer_id}, Last: {self.last_name}, First: " \
               f"{self.first_name}, Phone: {self.phone_number}, Address: {self.address}"

    def display(self):
        return f"Customer #{self.customer_id}:{self.last_name}, {self.first_name} \n" \
               f"{self.phone_number} in the verse\n" \
               f"{self.address}"
