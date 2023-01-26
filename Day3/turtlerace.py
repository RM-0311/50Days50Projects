import turtle as t


screen = t.Screen()
screen.setup(width=500, height=400)
screen.textinput(title="Make your bet",
                 prompt="Which turtle will win the race? Enter a color: ")

color_list = ["blue", "red", "yellow", "orange", "green", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tim = t.Turtle(shape="turtle")
    tim.color(color_list[turtle_index])
    tim.penup()
    tim.goto(x=x, y=y_positions[turtle_index])
    y += 30


screen.exitonclick()
