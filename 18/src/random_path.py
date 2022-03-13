from turtle import Screen, Turtle, colormode
from random import choice, randint

directions = [0, 90, 180, 270]
colormode(255)
turtle_1 = Turtle()
turtle_1.pensize(5)

def sequence(turtle):
  turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
  turtle.forward(10)
  turtle.setheading(choice(directions))

for turn in range(1000):
  print(f"Turn: {turn}")
  sequence(turtle_1)
  
screen = Screen()
screen.exitonclick()
