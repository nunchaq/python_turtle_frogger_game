from turtle import Turtle


class Lane(Turtle):

    def __init__(self, coord, color, width=3, height=31):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape("square")
        self.shapesize(width, height)
        self.setposition(coord)

    def dash(self):
        self.hideturtle()
        self.pensize(3)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
