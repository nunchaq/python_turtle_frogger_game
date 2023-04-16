from turtle import Turtle


class Frogger(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.color("black", "blue")
        self.setposition(0, -210)

    def restart(self):
        self.hideturtle()
        self.setposition(0, -210)
        self.showturtle()

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 10)

    def move_left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + 20, self.ycor())
