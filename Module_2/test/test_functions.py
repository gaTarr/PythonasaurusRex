import unittest
from intro_to_functions import camper_age_input


class MyTestCase(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(1, camper_age_input.convert_to_months(12))

    def test_positive(self):
        self.assertGreater(camper_age_input.convert_to_months(12), 0)


if __name__ == '__main__':
    unittest.main()
