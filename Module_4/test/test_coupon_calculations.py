"""CIS189 Python
Author: Greg Tarr
Created: 09/23/2019"""

import unittest
from store import coupon_calculations


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        assert coupon_calculations.calculate_order(9, 5, .1) == 9.77
        assert coupon_calculations.calculate_order(9, 5, .15) == 9.55
        assert coupon_calculations.calculate_order(9, 5, .2) == 9.34
        assert coupon_calculations.calculate_order(9, 10, .1) == 5.95
        assert coupon_calculations.calculate_order(9, 10, .15) == 5.95
        assert coupon_calculations.calculate_order(9, 10, .2) == 5.95


    def test_price_under_between_ten_thirty(self):
        assert coupon_calculations.calculate_order(15.99, 5, .1) == 18.43
        assert coupon_calculations.calculate_order(15.99, 5, .15) == 17.85
        assert coupon_calculations.calculate_order(15.99, 5, .2) == 17.27
        assert coupon_calculations.calculate_order(15.99, 10, .1) == 13.66
        assert coupon_calculations.calculate_order(15.99, 10, .15) == 13.35
        assert coupon_calculations.calculate_order(15.99, 10, .2) == 13.03

    def test_price_under_between_thirty_fifty(self):
        assert coupon_calculations.calculate_order(40, 5, .1) == 45.34
        assert coupon_calculations.calculate_order(40, 5, .15) == 43.48
        assert coupon_calculations.calculate_order(40, 5, .2) == 41.63
        assert coupon_calculations.calculate_order(40, 10, .1) == 40.57
        assert coupon_calculations.calculate_order(40, 10, .15) == 38.98
        assert coupon_calculations.calculate_order(40, 10, .2) == 37.39

    def test_price_over_fifty(self):
        assert coupon_calculations.calculate_order(70, 5, .1) == 62.01
        assert coupon_calculations.calculate_order(70, 5, .15) == 58.56
        assert coupon_calculations.calculate_order(70, 5, .2) == 55.12
        assert coupon_calculations.calculate_order(70, 10, .1) == 57.24
        assert coupon_calculations.calculate_order(70, 10, .15) == 54.06
        assert coupon_calculations.calculate_order(70, 10, .2) == 50.88


if __name__ == '__main__':
    unittest.main()
