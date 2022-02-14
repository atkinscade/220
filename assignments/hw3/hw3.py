"""
Name: Cade Atkins
hw4.py

Problem: Solve problems with an input and output using for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    value_list = []
    result = 0
    values = eval(input("How many values: "))
    for i in range(values):
        value = eval(input("Value: "))
        value_list.append(value)
    for i in value_list:
        result = result + i
    final_average = result / values
    print("The average is: ", final_average)


def tip_jar():
    result = 0
    tip_list = []
    for i in range(5):
        tips = eval(input("How much would you like to donate today? "))
        tip_list.append(tips)
    for i in tip_list:
        result = result + i
    print("Your total tip amount is: ", result)


def newton(num, root):
    # num = eval(input("What integer would you like to root: "))
    # root = eval(input("What root: "))
    for i in range(10):
        if i == 0:
            x = 1

    f = x ** root - num
    g = root * (x ** (root - 1))
    x = x - (f / g)
    return x
print(newton(531610, 2))


# def sequence():
#     num_sequence = eval(input("how many values would you like in your sequence: "))
#     odd_list = []
#     for i in range(0, num_sequence, 2):
#         if i == #odd
#             odd_list.append(i + 1)
#         else:
#             odd_list.append(i + 1)
#     print(odd_list)




def pi():
    pass


if __name__ == '__main__':
    pass
