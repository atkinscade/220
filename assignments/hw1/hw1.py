"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("enter the width: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    shots_made = eval(input("Enter how many shots were made: "))
    shots = eval(input("Enter shots total: "))
    shot_div = shots_made / shots
    print("Shooting Percentage: ", shot_div)




def coffee():
    lbs = eval(input("How many pounds of coffee would you like: "))
    cost = 12.11
    total = lbs * cost
    print("Your total is: ")


def kilometers_to_miles():
    kilos = eval(input("How many kilometers did you travel: "))
    kilo_in_mile = 1.61
    miles = kilos / kilo_in_mile
    print("That's", miles, "miles")


if __name__ == '__main__':
    pass
