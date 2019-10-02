"""CIS189 Python
Author: Greg Tarr
Created: 09/26/2019"""


numbers = []
user_input = 0
move_on = True
message = "Please enter a score (or -1 to stop): "
user_input = float(input(message))
while user_input != -1:
    while user_input <= 1 or user_input >= 100:
        user_input = float(input(message))
        if user_input == -1:
            move_on = False
            break
    if not move_on:
        break
    numbers.append(user_input)
    user_input = float(input(message))

for number in numbers:
    print(number)


# Please enter a score (or -1 to stop): 50
# Please enter a score (or -1 to stop): 33
# Please enter a score (or -1 to stop): 100
# Please enter a score (or -1 to stop): -1
# 50.0
# 33.0
#
# Process finished with exit code 0

# This one took me a little while to figure out!!
# I feel like i might be missing something, like there may be an easier method than this one..
