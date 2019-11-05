"""CIS189 Python
Author: Greg Tarr
Created: 11/04/2019"""
from customer import Customer


class Invoice:
    """Invoice Class"""

    # Constructor
    def __init__(self, inv_id, customer, items_price={}):
        if not isinstance(inv_id, int):
            raise AttributeError("'Invoice' object has no attribute 'cid'")
        self.invoice_id = inv_id
        self.customer = customer
        self.items_with_price = items_price

    def __str__(self):
        return f"Invoice Id:{self.invoice_id} Customer:{self.customer.display()}\n"

    def __repr__(self):
        return f"Invoice Id:{self.invoice_id} Customer:{self.customer.display()}\n"

    def add_item(self, new_item):
        """This provides a way to add more items and their prices to the order"""
        self.items_with_price.update(new_item)

    def create_invoice(self):
        """This creates an invoice based on prices of items
        :returns an itemized list of items and prices, tax, and the total"""
        tax = .06
        total = 0
        print(self.customer.display())
        for items, price in self.items_with_price.items():
            print(f"{items}.....${price:.2f}")
            total += price
        print(f"Tax....... {total*tax:.2f}")
        print(f"Total..... {total+(total*tax):.2f}")


if __name__ == '__main__':

    captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
    invoice = Invoice(1, captain_mal)
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
