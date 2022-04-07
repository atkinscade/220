from lab10.door import Door
from graphics import *
from random import randint

# win = GraphWin("3 Door Game", 600, 600)
# door_rec1 = Rectangle(Point(20, 100), Point(180, 530))
# door_rec2 = Rectangle(Point(220, 100), Point(380, 530))
# door_rec3 = Rectangle(Point(420, 100), Point(580, 530))
#
# win_point = Rectangle(Point(20, 10), Point(125, 80))
# lose_point = Rectangle(Point(20, 10), Point(230, 80))
#
# winning = Door(win_point, '0')
# losing = Door(lose_point, '0')
#
# door1 = Door(door_rec1, "Door 1")
# door2 = Door(door_rec2, "Door 2")
# door3 = Door(door_rec3, "Door 3")


def main():
    win = GraphWin("3 Door Game", 600, 600)
    door_rec1 = Rectangle(Point(20, 100), Point(180, 530))
    door_rec2 = Rectangle(Point(220, 100), Point(380, 530))
    door_rec3 = Rectangle(Point(420, 100), Point(580, 530))

    win_point = Rectangle(Point(20, 10), Point(125, 80))
    lose_point = Rectangle(Point(20, 10), Point(230, 80))

    winning = Door(win_point, '0')
    losing = Door(lose_point, '0')

    door1 = Door(door_rec1, "Door 1")
    door2 = Door(door_rec2, "Door 2")
    door3 = Door(door_rec3, "Door 3")

    ###
    secret = randint(1, 3)

    door1.open('green', 'Winner')

    time.sleep(5)

    door1.undraw()

    time.sleep(2)

    win.close()

main()



