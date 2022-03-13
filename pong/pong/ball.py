from turtle import Turtle
from random import choice

DIRECTIONS = [45, 135, 225, 315]

class Ball(Turtle):
  def __init__(self) -> None:
      super().__init__()
      self.shape("circle")
      self.color("white")
      self.penup()
      self.reset_position()

  def move(self):
    self.forward(1)

  def wall_bounce(self):
    if self.heading() == DIRECTIONS[0]:
      self.setheading(DIRECTIONS[3])
    elif self.heading() == DIRECTIONS[3]:
      self.setheading(DIRECTIONS[0])
    elif self.heading() == DIRECTIONS[1]:
      self.setheading(DIRECTIONS[2])
    elif self.heading() == DIRECTIONS[2]:
      self.setheading(DIRECTIONS[1])

  def paddle_bounce(self):
    if self.heading() == DIRECTIONS[0]:
      self.setheading(DIRECTIONS[1])
    elif self.heading() == DIRECTIONS[1]:
      self.setheading(DIRECTIONS[0])
    elif self.heading() == DIRECTIONS[2]:
      self.setheading(DIRECTIONS[3])
    elif self.heading() == DIRECTIONS[3]:
      self.setheading(DIRECTIONS[2])

  def reset_position(self):
    self.goto(0, 0)
    self.setheading(choice(DIRECTIONS))
