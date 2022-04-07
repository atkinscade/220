from lab10.door import Rec
from graphics import *
from random import randint


def main():
    done = False
    wins = 0
    losses = 0
    win = GraphWin("3 Door Game", 600, 600)

    while not done:

        door_rec1 = Rectangle(Point(20, 100), Point(180, 530))
        door_rec2 = Rectangle(Point(220, 100), Point(380, 530))
        door_rec3 = Rectangle(Point(420, 100), Point(580, 530))

        txt1 = 'Door 1'
        txt2 = 'Door 2'
        txt3 = 'Door 3'

        door1_txt = Text(Point(100, 300), txt1)
        door2_txt = Text(Point(300, 300), txt2)
        door3_txt = Text(Point(500, 300), txt3)

        exitting = Rectangle(Point(510, 10), Point(590, 90))

        win_point = Rectangle(Point(20, 10), Point(125, 80))
        lose_point = Rectangle(Point(20, 10), Point(230, 80))

        winning = Rec(win_point, Text(Point(70, 50), str(wins)))
        losing = Rec(lose_point, Text(Point(170, 50), str(losses)))

        door1 = Rec(door_rec1, door1_txt)
        door2 = Rec(door_rec2, door2_txt)
        door3 = Rec(door_rec3, door3_txt)

        exit_button = Rec(exitting, Text(Point(550, 50), "Exit"))

        ###
        secret = randint(1, 3)

        door1.draw(win)
        door2.draw(win)
        door3.draw(win)

        winning.draw(win)
        losing.draw(win)
        exit_button.draw(win)

        ###

        if secret == 1:
            door1.set_secret("True")
        elif secret == 2:
            door2.set_secret("True")
        else:
            door3.set_secret("True")

        click = win.getMouse()

        if door1.is_clicked(click):
            if door1.is_secret():
                door1.open('green', "correct")
                wins = wins + 1
                winning.undraw()
                winning.set_label(Text(Point(100, 300), wins))
                time.sleep(1)
                winning.draw(win)
                door1.close('white', 'Door 1')
            else:
                door1.open('red', 'incorrect')
                losses = losses + 1
                losing.undraw()
                losing.set_label(Text(Point(100, 300), losses))
                time.sleep(1)
                losing.draw(win)
                door1.close('white', 'Door 1')
        elif door2.is_clicked(click):
            if door2.is_secret():
                door2.open('green', "correct")
                wins = wins + 1
                winning.undraw()
                winning.set_label(Text(Point(300, 300), wins))
                time.sleep(1)
                winning.draw(win)
                door2.close('white', 'Door 1')
            else:
                door2.open('red', "incorrect")
                losses = losses + 1
                losing.undraw()
                losing.set_label(Text(Point(300, 300), losses))
                time.sleep(1)
                losing.draw(win)
                door2.close('white', 'Door 2')
        elif door3.is_clicked(click):
            if door3.is_secret():
                door3.open('green', "correct")
                wins = wins + 1
                winning.undraw()
                winning.set_label(Text(Point(500, 300), wins))
                time.sleep(1)
                winning.draw(win)
                door3.close('white', 'Door 3')
            else:
                door3.open('red',  "incorrect")
                losses = losses + 1
                losing.undraw()
                losing.set_label(Text(Point(500, 300), losses))
                time.sleep(1)
                losing.draw(win)
                door3.close('white', 'Door 3')
        elif exit_button.is_clicked(click):
            exit_button.color_door("red")
            done = True
            time.sleep(1)
            win.close()

main()