from graphics import *
# sum function for personal use
def summ(sum_list):
    result = 0
    for i in sum_list:
        result = result + i
    return result


def triangle():
    placeholder = 400
    triangle_win = GraphWin('triangle', 400, 400)
    directions = Text(Point(75, 20), "Click 3 points in the window")
    directions.draw(triangle_win)
    point_1 = triangle_win.getMouse()
    point_2 = triangle_win.getMouse()
    point_3 = triangle_win.getMouse()
    x_1 = int(point_1.getX())
    x_2 = int(point_2.getX())
    x_3 = int(point_3.getX())
    y_1 = int(point_1.getY())
    y_2 = int(point_2.getY())
    y_3 = int(point_3.getY())
    in_draw = Polygon(Point(x_1, y_1), Point(x_2, y_2), Point(x_3, y_3))
    in_draw.draw(triangle_win)
    line_a = (((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)) ** 0.5
    line_b = (((x_3 - x_2) ** 2) + ((y_3 - y_2) ** 2)) ** 0.5
    line_c = (((x_1 - x_3) ** 2) + ((y_1 - y_3) ** 2)) ** 0.5
    sum_list = [line_c, line_b, line_a]
    perimeter = Text(Point(75, 60), str(summ(sum_list)))
    area = Text(Point(75, 40),  str(summ(sum_list)/2))
    area.draw(triangle_win)
    perimeter.draw(triangle_win)
    input("enter/return to close")
    triangle_win.close()



def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user = input("Enter a string: ")
    print(user[0])
    print(user[-1])
    print(user[1:5])
    print(user[0] + user[-1])
    print(user[-3:]* 10)
    for letter in user:
        print(letter)
    print(len(user))


def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    x = summ(x)
    print(x)
    print(len(values))




def another_series():
    num_sequence = eval(input("How many numbers in your series: "))
    sequence_list = []
    for i in range(num_sequence):
        for j in range(1, 7, 2):
            sequence_list.append(j+1)
    result = sequence_list[0:num_sequence]
    print(result, "sum: " , summ(result))

another_series()




def target():
    color_list = ["white", "black", "blue", "red", "yellow"]

    target_win = GraphWin("Target", 400, 400)
    center = Point(200, 200)
    for i in range(5):
        place_holder = 200
        place_holder =  place_holder - i * 40
        target_circle = Circle(center, place_holder)
        target_circle.setFill(color_list[i])
        target_circle.draw(target_win)
    input("enter/return to close")
    target_win.close()
