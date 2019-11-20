"""CIS189 Python
Author: Greg Tarr
Created: 10/15/2019"""
import tkinter


def pick_breakfast():
    label.config(text="Too Early!!")


def pick_breakfast_2():
    label.config(text="That's Better :)")


def pick_lunch():
    label.config(text="What about elevensies..?")


def pick_dinner():
    label.config(text="Save room for Dessert!")


meals = tkinter.Tk()
meals.title('Favorite Meal')
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(meals, text='Breakfast', variable=var1, command=pick_breakfast).grid(row=1)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(meals, text='Second Breakfast', variable=var2, command=pick_breakfast_2).grid(row=2)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(meals, text='Lunch', variable=var3, command=pick_lunch).grid(row=3)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(meals, text='Dinner', variable=var4, command=pick_dinner).grid(row=4)
label = tkinter.Label(meals, text="Waiting")
label.grid(row=5)
exit_button = tkinter.Button(meals, text='Exit', width=25, command=meals.destroy)
exit_button.grid(row=6)
meals.mainloop()
