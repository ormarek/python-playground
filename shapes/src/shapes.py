from turtle import Screen, Turtle, colormode
from random import randint

turtle = Turtle()
colormode(255)

def starting_position():
  turtle.penup()
  turtle.left(90)
  turtle.forward(250)
  turtle.left(90)
  turtle.forward(25)
  turtle.right(180)
  turtle.pendown()

def draw_shape(sides):
  angle = 360/sides
  turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
  for _ in range(sides):
    turtle.forward(50)
    turtle.right(angle)

starting_position()

for shape in range(3, 20):
  draw_shape(shape)

screen = Screen()
screen.exitonclick()
