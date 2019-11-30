"""CIS189 Python
Author: Greg Tarr
Created: 11/26/2019"""
from connect_to_database import *
import tkinter as t

# Declare Database
db_name = 'assignment.db'


def add_person():
    '''This gets the db name, creates a connection and passes the connection
    to add a person method'''
    global db_name
    conn = create_connection(db_name)
    with conn:
        person_input = (person_first_name.get(), person_last_name.get())
        person_id = create_person(conn, person_input)


def add_student():
    '''This gets the db name, creates a connection and passes the connection
    to add a student method'''
    global db_name
    conn = create_connection(db_name)
    with conn:
        person_input = (student_first_name.get(), student_last_name.get())
        # print(select_student_by_name(conn, person_input))
        student_input = (select_student_by_name(conn, person_input), student_maj.get(), student_st_dt.get())
        print(student_input)
        student_id = create_student(conn, student_input)


def view_persons():
    '''This creates a display window and a database connection, then passes
    the connection to select_all_persons. Finally, it displays all rows returned
    by select_all_persons in the window.'''
    display_frame_persons = t.Tk()
    display_frame_persons.title('Display Persons')
    display_row = 2
    conn = create_connection(db_name)
    with conn:
        rows = select_all_persons(conn)
        for row in rows:
            display_label = t.Label(display_frame_persons, text=row)
            display_label.grid(row=display_row)
            display_row += 1


def view_students():
    '''This creates a display window and a database connection, then passes
    the connection to select_all_students. Finally, it displays all rows returned
    by select_all_students in the window.'''
    display_frame_students = t.Tk()
    display_frame_students.title('Display Students')
    display_row = 2
    conn = create_connection(db_name)
    with conn:
        rows = select_all_students(conn)
        for row in rows:
            display_label = t.Label(display_frame_students, text=row)
            display_label.grid(row=display_row)
            display_row += 1


# Create GUI
frame = t.Tk()
frame.title('Database Objects')
frame.geometry('800x800')

# Create Buttons
create = t.Button(frame, text='Create Database & Table', width=20, command=lambda: create_tables(db_name))
create.grid(row=2, column=1, pady=4)

add_person = t.Button(frame, text='Add Person', width=20, command=add_person)
add_person.grid(row=6, column=1, pady=4)

add_student = t.Button(frame, text='Add Student', width=20, command=add_student)
add_student.grid(row=10, column=1, pady=4)

view_person = t.Button(frame, text='View Person Table', width=20, command=view_persons)
view_person.grid(row=14, column=1, pady=4)

view_student = t.Button(frame, text='View Student Table', width=20, command=view_students)
view_student.grid(row=18, column=1, pady=4)

# Collect Input
person_ln_label = t.Label(frame, text="Last Name")
person_ln_label.grid(row=6, column=2)
person_last_name = t.Entry(frame, bd=4, justify='center')
person_last_name.grid(row=6, column=3)

person_fn_label = t.Label(frame, text="First Name")
person_fn_label.grid(row=7, column=2)
person_first_name = t.Entry(frame, bd=4, justify='center')
person_first_name.grid(row=7, column=3)

student_ln_label = t.Label(frame, text="Last Name")
student_ln_label.grid(row=10, column=2)
student_last_name = t.Entry(frame, bd=4, justify='center')
student_last_name.grid(row=10, column=3)

student_fn_label = t.Label(frame, text="First Name")
student_fn_label.grid(row=11, column=2)
student_first_name = t.Entry(frame, bd=4, justify='center')
student_first_name.grid(row=11, column=3)

student_maj_label = t.Label(frame, text="Major")
student_maj_label.grid(row=12, column=2)
student_maj = t.Entry(frame, bd=4, justify='center')
student_maj.grid(row=12, column=3)

student_st_dt_label = t.Label(frame, text="Start Date")
student_st_dt_label.grid(row=13, column=2)
student_st_dt = t.Entry(frame, bd=4, justify='center')
student_st_dt.grid(row=13, column=3)

frame.mainloop()

if __name__ == '__main__':
    conn = create_connection(db_name)
    with conn:
        rows = select_all_students(conn)
        for row in rows:
            print(row)
