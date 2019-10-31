"""CIS189 Python
Author: Greg Tarr
Created: 10/29/2019"""


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError
        if not (isinstance(gpa, float) and (0.0 <= gpa <= 4.0)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

    def display(self):
        return self.last_name + ", " + self.first_name + ":" + self.major + " gpa: " + str(self.gpa)


if __name__ == '__main__':
    # Driver

    student1 = Student('Duck', 'Donald', 'Speech Therapy') # ssn not required
    print(student1.display())
    # Valid person and ssn
    student2 = Student('Duck', 'Donald', 'Speech Therapy', 2.1)
    print(student2.display())
    # Invalid person
    # Wait! try/except needed!
    try:
        student3 = Student('123', 'Donald', 'Speech Therapy', 2.1)
    except ValueError:
        print("Error found, person not created")


