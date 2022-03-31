
class Button:

    def __init__(self, shape, text):
        self.shape = shape
        self.text = text

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

    def color_button(self, color):
        self.shape.setFill(color)

