# import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract('images.jpg', 143)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(239, 234, 84), (208, 159, 101), (188, 10, 67), (115, 177, 204), (26, 115, 167), (216, 133, 166), (175, 170, 29), (166, 78, 35), (131, 185, 148), (219, 66, 111), (9, 30, 75), (35, 135, 81), (171, 50, 95), (232, 74, 45), (235, 229, 4), (233,
                                                                                                                                                                                                                                                          165, 192), (78, 10, 60), (11, 50, 29), (26, 165, 206), (61, 167, 100), (18, 42, 134), (138, 213, 228), (9, 100, 64), (134, 33, 19), (91, 29, 11), (160, 208, 183), (228, 175, 165), (253, 5, 53), (8, 91, 105), (67, 133, 198), (114, 92, 4), (179, 188, 212)]
t.colormode(255)
tim = t.Turtle("turtle")
tim.color("Green")
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()

screen = t.Screen()
screen.exitonclick()
