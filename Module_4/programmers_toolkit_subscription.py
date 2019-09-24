"""CIS189 Python
Author: Greg Tarr
Created: 09/02/2019"""


if __name__ == '__main__':
    print("Welcome to the Programmer's Toolkit Monthly Subscription!")
    selection = int((input("Choose your subscription level (enter number): "
                          "\n1. Platinum"
                          "\n2. Gold"
                          "\n3. Silver"
                          "\n4. Bronze"
                          "\n5. Free Trial"
                           "\nSelection: ")))

    if selection == 1:
        print("You chose Platinum, the cost is $60!")
    elif selection == 2:
        print("You chose Gold, the cost is $50!")
    elif selection == 3:
        print("You chose Silver, the cost is $40!")
    elif selection == 4:
        print("You chose Bronze, the cost is $30!")
    elif selection == 5:
        print("You chose Free Trial, the cost is Free!")
    else:
        print("Invalid Input!")

