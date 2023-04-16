from turtle import Turtle
import random


class Car(Turtle):

    def __init__(self, speed, coord, direction):
        super().__init__()
        self.penup()
        self.color("black",(random.randint(50, 230), random.randint(50, 230), random.randint(50, 230)))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.car_speed = speed
        self.direction = direction
        self.coord = coord
        self.setposition(self.coord)

    def move(self):
        if self.direction:
            self.backward(self.car_speed)
        else:
            self.forward(self.car_speed)

        if self.xcor() < -350 and self.direction:
            self.setposition(self.coord)

        if self.xcor() > 350 and not self.direction:
            self.setposition(self.coord)
