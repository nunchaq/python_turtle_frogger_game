from turtle import Turtle


class Score(Turtle):
    lives = 3
    level = 1
    font_size = 22
    font = ("Arial", font_size, "normal")

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 150)
        self.show_lives()

    def show_lives(self):
        self.write("Level " + str(self.level) + " Lives: " + str(self.lives), False, align="center", font=self.font)

    def take_a_life(self):
        self.lives -= 1
        self.clear()

    def game_over(self):
        self.setposition(0, 0)
        self.font_size = 35
        self.write("GAME OVER", False, align="center", font=self.font)

    def next_level(self):
        self.level += 1
        self.clear()
