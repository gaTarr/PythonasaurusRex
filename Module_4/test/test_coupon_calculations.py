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


if __name__ == '__main__':
    unittest.main()
