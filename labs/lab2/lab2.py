"""
Cade Atkins
lab2.py

Q: Implement a function that calculates the RMS, Harmonic Mean, and Geometric mean of an inputted value

I certify that this assignment is entirely my own work.
"""

def means():
    values = eval(input("How many values will you enter: "))
    result = 1
    value_list = []
    one_over_x_list = [] # for harmonic mean
    x_squared_list = [] # for rms mean
    for i in range(values): # create list of values
        value = eval(input("Value: "))
        value_list.append(value)
    for i in value_list: # harmonic mean
        one_over_x = (1 / i)
        one_over_x_list.append(one_over_x)
    for i in value_list: # rms mean
        x_squared = i ** 2
        x_squared_list.append(x_squared)
    for i in value_list: # geometric mean
        result = result * i

    sum_list_harmonic = sum(one_over_x_list)
    sum_list_rms = sum(x_squared_list)
    geometric = float(result)

    print("Harmonic Mean: ", values / sum_list_harmonic)
    print("Root-Mean-Square: ", (sum_list_rms / values) ** (1/2))
    print("Geometric Mean: ", geometric ** (1.0 / values))


means()


