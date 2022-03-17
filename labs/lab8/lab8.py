from graphics import *
from random import randint


def delay(d):
    for _ in range(d):
        for _ in range(50):
            pass


def get_random(num):
    randint(0, num)


def close(win):
    input(" ")
    win.close()
    return


def did_collide(self, other):
    self_rad = self.getRadius()
    other_rad = other.getRadius()
    self = self.getCenter()
    other = other.getCenter()
    distance = ((self.getX() - other.getX()) ** 2) + ((self.getY() - other.getY()) ** 2) ** 0.5
    print(distance)
    if distance > (self_rad - other_rad / 2.0):
        return print(True)
    else:
        return print(False)


def hit_vertical(self, win):
    constant = 0
    height = win.getHeight()
    self_center = self.getCenter()
    if self_center == constant or height:
        return True
    else:
        return False


def hit_horizontal(other, win):
    constant = 0
    width = win.getWidth()
    other_center = other.getCenter()
    if other_center.getX() == constant or width:
        return True
    else:
        return False


def random_color():
    return color_rgb(randint(0, 256), randint(0, 256), randint(0, 256))

def main():
    win = GraphWin("Joyride", 400, 400)
    self = Circle(Point(randint(0, 400), randint(0, 400)), 10)
    self.setFill(random_color())
    self.draw(win)
    other = Circle(Point(randint(0, 400), randint(0, 400)), 10)
    other.setFill(random_color())
    other.draw(win)
    while True:
        self.move(get_random())

