from turtle import Turtle, Screen

class Paddle(Turtle):
  def __init__(self,xcor,ycor):
    super().__init__()
    self.shape("square")
    self.speed(10.5)
    self.color("white")
    self.shapesize(stretch_len=1, stretch_wid=5)
    self.penup()
    self.goto(xcor,ycor)

  def go_up(self):
    new_y = self.ycor() + 30
    self.goto(self.xcor(), new_y)

  def go_down(self):
    new_y = self.ycor() - 30
    self.goto(self.xcor(), new_y)