# import colorgram #helps to extract colors
import turtle as t
import random

# colors = colorgram.extract("img.jpg", 10)
# # print(colors)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color_rgb = (r,g,b)
#     rgb_colors.append(new_color_rgb)

# print(rgb_colors)
# Extracted color list
color_list = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168,
                                                                                                             40), (184, 158, 46)]


tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)

tim.pensize(20)
tim.speed('fastest')

tim.hideturtle()
tim.penup()
x = -300
y = -300
tim.setposition(x, y)

def line():
    for i in range(11):
        tim.color(random.choice(color_list))
        tim.forward(4)
        tim.penup()
        tim.forward(50)
        tim.pendown()

def next_line():
    tim.penup()
    global y
    y += 50
    tim.setposition(x, y)
    line()

for i in range(10):
    next_line()

screen.exitonclick()
