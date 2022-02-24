from graphics import *

def vignere():
    win = GraphWin("Vignere", 550, 400)
    win.setBackground("white")
    input_text = Text(Point(50, 100), "Message to Code: ")
    key_text = Text(Point(50, 135), "Enter Keyword: ")
    key_text.draw(win)
    input_text.draw(win)
    input_entry = Entry(Point(200, 100), 25)
    key_entry = Entry(Point(150, 135), 10)
    key_entry.draw(win)
    input_entry.draw(win)

# encode box
    encode_box = Rectangle(Point(225, 335), Point(325, 365))
    encode_box.draw(win)
# encode box text
    box_txt = Text(Point(255, 350), "Encode")
    box_txt.draw(win)
# input retrieval
    win.getMouse()
    msg = input_entry.getText()
    msg = msg.upper().replace(" ", "")
    key = key_entry.getText()
    key = key.upper().replace(" ", "")
# cipher
    output_txt = ''
    key_len = len(key)
    int_key = [ord(i) for i in key]
    int_msg = [ord(i) for i in msg]
    for i in range(len(msg)):
        result = (int_msg[i] + int_key[i % key_len]) % 26
        output_txt += chr(result + 65)
# output
    encode_box.move(1000, 1000)
    box_txt.move(1000, 1000)

    output_msg = Text(Point(275, 350), "Encoded: ")
    encoded_msg = Text(Point(275, 370), output_txt)
    output_msg.draw(win)
    encoded_msg.draw(win)


    win.getMouse()
    win.close()

vignere()
