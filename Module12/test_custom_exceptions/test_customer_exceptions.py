import unittest
from custom_exceptions import customer_exceptions as ce


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_customer_id_out_of_range(self):
        with self.assertRaises(ce.InvalidCustomerIdException):
            test_customer = ce.Customer(55566, "Tarr", "Greg", "515-123-4567")

    def test_customer_last_name_with_symbol(self):
        with self.assertRaises(ce.InvalidNameException):
            test_customer = ce.Customer(5556, "Ta%rr", "Greg", "515-123-4567")

    def test_customer_first_name_with_number(self):
        with self.assertRaises(ce.InvalidNameException):
            test_customer = ce.Customer(5556, "Tarr", "Gre33g", "515-123-4567")

    def test_customer_phone_with_invalid_format(self):
        with self.assertRaises(ce.InvalidPhoneNumberFormat):
            test_customer = ce.Customer(5556, "Tarr", "Greg", "(515)123-4567")

    def test_customer_str_valid(self):
        test_customer = ce.Customer(5556, "Tarr", "Greg", "515-123-4567")

        expected_result = 'Customer Id: 5556, Last: Tarr, First: Greg, Phone: 515-123-4567'
        self.assertEqual(test_customer.__str__(), expected_result)


if __name__ == '__main__':
    unittest.main()
