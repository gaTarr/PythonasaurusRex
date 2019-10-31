import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Tarr', 'Greg', 'CIS')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Tarr')
        self.assertEqual(self.student.first_name, 'Greg')
        self.assertEqual(self.student.major, 'CIS')

    def test_object_created_all_attributes(self):
        student = s.Student('Tarr', 'Greg', 'CIS', 4.0)
        assert student.last_name == 'Tarr'
        assert student.first_name == 'Greg'
        assert student.major == "CIS"
        assert student.gpa == 4.0

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Tarr, Greg has major CIS with gpa: 0.0')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            invalidStudet = s.Student('123', 'Greg', 'CIS')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            invalidStudent = s.Student('Tarr', '123', 'CIS')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            invalidStudent = s.Student('Tarr', 'Greg', '123')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            invalidStudent = s.Student('Tarr', 'Greg', 'CIS', '234')

    def test_gpa_out_of_range(self):
        with self.assertRaises(ValueError):
            invalidStudent = s.Student('Tarr', 'Greg', 'CIS', 4.1)
        with self.assertRaises(ValueError):
            invalidStudent2 = s.Student('Tarr', 'Greg', 'CIS', -1)



if __name__ == '__main__':
    unittest.main()
