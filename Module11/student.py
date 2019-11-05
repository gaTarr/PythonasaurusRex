"""CIS189 Python
Author: Greg Tarr
Created: 11/04/2019"""
from person import Person


class Student(Person):
    """Student class"""

    def __init__(self, student_id, last_name, first_name, major='Computer Science', gpa=0.0):
        valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()/'-, ")
        if not isinstance(gpa, float):
            raise AttributeError("Invalid GPA")
        if not isinstance(student_id, int):
            raise ValueError
        if not (valid_characters.issuperset(last_name) and
                valid_characters.issuperset(first_name) and
                valid_characters.issuperset(major)):
            raise ValueError
        super().__init__(last_name, first_name)
        self._student_id = student_id
        self._major = major
        self._gpa = gpa

    def change_major(self, new_major):
        """This takes a value and assigns it to the major variable
        :param new_major: This is the value that will be assigned to major variable"""
        self._major = new_major

    def update_gpa(self, new_gpa):
        """This takes a value and assigns it to the gpa variable
        :param new_gpa: This is the value that will be assigned to gpa variable"""
        self._gpa = new_gpa

    def display(self):
        """This returns values assigned to class variables"""
        return f"{self.last_name}, {self.first_name}:({self._student_id}) {self._major} gpa: {self._gpa}"


if __name__ == '__main__':

    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student
