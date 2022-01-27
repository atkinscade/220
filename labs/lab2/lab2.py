"""
Cade Atkins
lab2.py

Q: Implement a function that calculates the RMS, Harmonic Mean, and Geometric mean of an inputted value

I certify that this assignment is entirely my own work.
"""

def means():
    values = eval(input("How many values will you enter: "))
    value_list = []
    one_over_x_list = []
    for i in range(values): ### create list of values
        value = eval(input("Value: "))
        value_list.append(value)
    for i in value_list: ### harmonic mean
        one_over_x = (1 / i)
        one_over_x_list.append(one_over_x)
    sum_list = sum(one_over_x_list)




    print("Harmonic Mean: ", values / sum_list)




