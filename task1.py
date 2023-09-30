class Widget:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
    def print_info(self):
        print(self.text)
class Button(Widget):
    def __init__(self, x, y, text):
        super().__init__(x, y, text)
        self.clicked = False

    def click(self):
        self.clicked = True
        
btn1 = Button (2,2, "qwe123")

btn1.print_info()




