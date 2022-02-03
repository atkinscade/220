"""
Name: Cade Atkins
lab3.py

Problem: Solve traffic average with an input and output using for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def summ(itlist):
    result = 0
    for i in itlist:
        result = result + i
    return result

def traffic():
    total_cars = []
    road_num = eval(input("Roads surveyed: "))
    for i in range(road_num):
        print("How many days was road ", i + 1, ' surveyed: ')
        days_surveyed = eval(input(''))
        car_list = []
        for j in range(days_surveyed):
            print("\tHow many cars traveled on day", j + 1, ": ")
            cars_on = eval(input(''))
            car_list.append(cars_on)
            total_cars.append(cars_on)
        average_cars = summ(car_list) / days_surveyed
        print("Road ", i + 1, " averaged vehicles per day: ", average_cars)
    print("Total number of vehicles traveled on all roads: ", summ(total_cars))
    print("Average number of vehicles per road: ", summ(total_cars) / road_num)

