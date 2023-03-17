import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=2)
        self.color("black")
        y_cord = random.randint(-250, 250)
        self.goto(500, y_cord)

    def move(self):
        new_x = self.xcor() + MOVE_INCREMENT
        self.goto(new_x, self.ycor())
