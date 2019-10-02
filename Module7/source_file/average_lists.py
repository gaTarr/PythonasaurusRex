"""docstring with name"""


def average(a_list):
    return sum(a_list) / len(a_list)


def average2(*args, **kwargs):
    for a in args: #will need to replace this part with the logic to calculate average
        print(a)
    for key, value in kwargs.items():
        print("key is " + key + " value is " + value)
    # return


if __name__ == '__main__':
    # print(average([2, 3, 5]))

    print(average2(2, 3, 5, first_name = 'Greg', last_name = 'Tarr'))
    print(average2(3.4, 3.3, 5.6, 2.67))
