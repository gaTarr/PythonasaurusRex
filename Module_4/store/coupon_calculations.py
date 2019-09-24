"""CIS189 Python
Author: Greg Tarr
Created: 09/23/2019"""


def calculate_tax(subtotal):
    tax = .06
    return subtotal + (subtotal * tax)


def calculate_subtotal(price, cash, percent):
    return (price - cash) - ((price - cash) * percent)


def calculate_order(price, cash_coupon, percent_coupon):
    if price < 10:
        if cash_coupon == 5:
            if percent_coupon == .1:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 5.95), 2)
            elif percent_coupon == .15:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 5.95), 2)
            elif percent_coupon == .2:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 5.95), 2)
            else:
                print("Invalid coupon Percentage.")
        elif cash_coupon == 10:
            if percent_coupon == .1 or percent_coupon == .15 or percent_coupon == .2:
                return 5.95
            else:
                print("Invalid coupon Percentage.")
    elif 10 < price < 30:
        if cash_coupon == 5:
            if percent_coupon == .1:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 7.95), 2)
            elif percent_coupon == .15:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 7.95), 2)
            elif percent_coupon == .2:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 7.95), 2)
            else:
                print("Invalid coupon Percentage.")
        elif cash_coupon == 10:
            if percent_coupon == .1:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 7.95), 2)
            elif percent_coupon == .15:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 7.95), 2)
            elif percent_coupon == .2:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 7.95), 2)
            else:
                print("Invalid coupon Percentage.")
    elif 30 < price < 50:
        if cash_coupon == 5:
            if percent_coupon == .1:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 11.95), 2)
            elif percent_coupon == .15:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 11.95), 2)
            elif percent_coupon == .2:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 11.95), 2)
            else:
                print("Invalid coupon Percentage.")
        elif cash_coupon == 10:
            if percent_coupon == .1:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 11.95), 2)
            elif percent_coupon == .15:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 11.95), 2)
            elif percent_coupon == .2:
                return round((calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)) + 11.95), 2)
            else:
                print("Invalid coupon Percentage.")
    elif price > 50:
        if cash_coupon == 5:
            if percent_coupon == .1:
                return round(calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)), 2)
            elif percent_coupon == .15:
                return round(calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)), 2)
            elif percent_coupon == .2:
                return round(calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)), 2)
            else:
                print("Invalid coupon Percentage.")
        elif cash_coupon == 10:
            if percent_coupon == .1:
                return round(calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)), 2)
            elif percent_coupon == .15:
                return round(calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)), 2)
            elif percent_coupon == .2:
                return round(calculate_tax(calculate_subtotal(price, cash_coupon, percent_coupon)), 2)
            else:
                print("Invalid coupon Percentage.")
    else:
        print("Error handling for Price out of bounds")


if __name__ == '__main__':
    pass
