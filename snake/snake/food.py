from turtle import Turtle
from random import randint
from math import ceil

class Food(Turtle):
  def __init__(self) -> None:
      super().__init__()
      self.shape("circle")
      self.shapesize(0.5, 0.5)
      self.color("blue")
      self.speed("fastest")
      self.penup()
      self.set_pos()

  def set_pos(self):
    x = int(ceil(randint(-140, 140) / 10.0)) * 20
    y = int(ceil(randint(-140, 140) / 10.0)) * 20
    self.goto(x, y)
