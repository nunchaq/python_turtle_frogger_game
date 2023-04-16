from turtle import Screen
from Map import Map
from Car import Car
from Frogger import Frogger
from Score import Score
import time, random

lanes = {
    "right": [-105, -15, 75, 165],
    "left": [-145, -55, 35, 125]
}

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("gray")
screen.title("Frogger")
screen.tracer(0)
screen.colormode(255)

Map()


def render_cars():
    cars = []
    for lane in lanes["right"]:
        speed = random.randint(4, 11)
        for x in range(1000, 350, random.randint(140, 200) * -1):
            cars.append(Car(speed, (x, lane), 1))

    for lane in lanes["left"]:
        speed = random.randint(4, 11)
        for x in range(-1000, -350, random.randint(140, 200) * 1):
            cars.append(Car(speed, (x, lane), 0))
    return cars


cars = render_cars()

frogger = Frogger()
screen.listen()
screen.onkey(key="Up", fun=frogger.move_up)
screen.onkey(key="Down", fun=frogger.move_down)
screen.onkey(key="Left", fun=frogger.move_left)
screen.onkey(key="Right", fun=frogger.move_right)



score = Score()
is_playing = True
while is_playing:
    time.sleep(0.1)
    screen.update()
    score.show_lives()

    for car in cars:
        car.move()

        if frogger.distance(car) < 20 and abs(frogger.xcor() - car.xcor()) < 15:
            frogger.restart()
            score.take_a_life()

        if score.lives == 0:
            is_playing = False
            score.game_over()

        if frogger.ycor() > 200:
            score.next_level()
            frogger.restart()

            for x in cars:
                x.hideturtle()

            cars = render_cars()

        if score.level == 10:
            is_playing = False
            score.game_over()

screen.exitonclick()
