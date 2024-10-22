# import colorgram
#
# colour = colorgram.extract('image.jpg', 50)
#
# rgb_color = []
#
# for color in colour:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new = (r, g, b)
#     rgb_color.append(new)
#
# print(rgb_color)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")

colors = [(235, 228, 211), (217, 218, 223), (104, 106, 125), (213, 152, 91), (140, 140, 150), (186, 62, 32), (225, 212, 109), (199, 147, 173), (237, 215, 225), (105, 112, 170), (177, 159, 47), (218, 224, 219), (186, 19, 9), (38, 40, 21), (27, 25, 63), (26, 42, 22), (223, 167, 194), (42, 44, 101), (205, 87, 58), (58, 68, 54), (132, 136, 132), (190, 187, 218), (230, 176, 172), (231, 65, 82)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
dot_count = 100

for dot in range(1, dot_count + 1):
    tim.dot(24, random.choice(colors))
    tim.forward(50)
    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
