"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def add_ten(nums):
    plus10 = []
    for i in nums:
        new_num = i + 10
        plus10.append(new_num)
    return plus10



def square_each(nums):
    new_list = []
    for i in nums:
        new_num = i ** 2
        new_list.append(new_num)
    return new_list


def sum_list(nums):
    result = 0
    for i in nums:
        result += i
    return result


def to_numbers(nums):
    new_list = []
    for i in nums:
        if '.' not in i:
            new_list.append(int(i))
        else:
            new_list.append(float(i))
    return new_list



def sum_of_squares(nums):
    pass


def starter(weight, wins):
    pass


def leap_year(year):
    pass


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    pass


if __name__ == '__main__':
    pass
