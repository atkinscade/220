
class Rec:
    def __init__(self, shape, text):
        self.shape = shape
        self.text = text
        self.secret = False

    def get_label(self):
        return self.text

    def set_label(self, label):
        self.text = label

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        if point in self.shape:
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if not self.secret:
            return False
        else:
            return True

    def set_secret(self, secret):
        self.secret = secret


