import turtle as t
import random


screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")

color_list = ["blue", "red", "yellow", "orange", "green", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color_list[turtle_index])
    new_turtle.speed("fast")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = (turtle.fillcolor())
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if winner == user_bet:
    print("You won!")
else:
    print(
        f"You guessed the incorrect turtle. {winner} was the winning color turtle.")
screen.exitonclick()
