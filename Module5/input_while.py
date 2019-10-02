"""CIS189 Python
Author: Greg Tarr
Created: 09/26/2019"""


numbers = []
user_input = 0
message = "Please enter a score (or -1 to stop): "
user_input = float(input(message))
while user_input != -1:
    while user_input <= 1 or user_input >= 100:
        user_input = float(input(message))
    numbers.append(user_input)
    user_input = float(input(message))

for number in numbers:
    print(number)


# Please enter a score (or -1 to stop): 5
# Please enter a score (or -1 to stop): 3
# Please enter a score (or -1 to stop): 7
# Please enter a score (or -1 to stop): -1
# 5.0
# 3.0
# 7.0
#
# Process finished with exit code 0

# Simple enough, the same as other languages, but nice that it can be run as a script
# in the shell.  I wanted to find a condensed way to write the inner while statement
