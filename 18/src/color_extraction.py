import colorgram
import random
from turtle import Screen, Turtle, colormode

color_list = []
colors = colorgram.extract('assets/image.jpeg', 100)

for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  color_list.append((r, g, b))

colormode(255)
turtle = Turtle()
screen = Screen()
screensize_x = screen.screensize()[0]
screensize_y = screen.screensize()[1]

move_by_x = screensize_x / 10
move_by_y = screensize_y / 10

starting_position_x = -screensize_x / 2
starting_position_y = -screensize_y / 2

turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.setpos(starting_position_x, starting_position_y)

for index in range(0, 100):
  current_x = turtle.position()[0]
  current_y = turtle.position()[1]
  turtle.dot(20, random.choice(color_list))
  turtle.setheading(0)

  if (index + 1) % 10 == 0:
    turtle.setposition(starting_position_x, current_y + move_by_y)
  else:
    turtle.setposition(current_x + move_by_x, current_y)

screen.exitonclick()
