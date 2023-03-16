from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

score_l = Scoreboard((-80, 200))
score_r = Scoreboard((80, 200))

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 330 or ball.distance(l_paddle) < 60 and ball.xcor() < -330:
        ball.bounce_x()
        ball.move_speed *= 0.9

    # Detect if ball goes out of bounds
    if ball.xcor() > 380:
        ball.goto(0,0)
        ball.bounce_x()
        score_l.increase_score()
        time.sleep(1)
        ball.move_speed = 0.1
        if score_l.score == 10:
            game_is_on = False

    if ball.xcor() < -380:
        ball.goto(0,0)
        ball.bounce_x()
        score_r.increase_score()
        time.sleep(1)
        if score_r.score == 10:
            game_is_on = False

        

screen.exitonclick()