"""
Name: Cade Atkins
lab4.py

Problem: Cute little V-day message

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def greeting_card():
    win = GraphWin("Valentine's", 700, 700)
    win.setBackground('pink')
    heart = Polygon(Point(600, 200), Point(540, 115), Point(475, 200),Point(410, 115), Point(350, 200), Point(475, 370))
    #point               1                  2                3                 4                 5               6
    arrow = Polygon(Point(0,0), Point(0, 36), Point(10, 21), Point(100, 21), Point(100, 36), Point(130, 18), Point(100, 0), Point(100, 15), Point(10, 15))
    vday_msg = Text(Point(200, 300), "Happy Valentines Day")
    vday_msg.setFace('times roman')
    vday_msg.setTextColor('black')
    vday_msg.setSize(36)
    vday_msg.draw(win)
    heart.draw(win)
    arrow.draw(win)
    heart.setFill('red')
    arrow.setFill('brown')
    arrow.move(150, 600)
    for i in range(300):
        arrow.move(0, -2)
        time.sleep(0.02)
        arrow.move(1, 0)
    win.close()
