from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, x: int = ...) -> None:
      super().__init__()
      self.initial_x = x
      self.shape("square")
      self.shapesize(stretch_wid=5, stretch_len=1)
      self.color("white")
      self.penup()
      self.reset_position()

  def up(self):
    self.goto(self.xcor(), self.ycor() + 20)
  
  def down(self):
    self.goto(self.xcor(), self.ycor() - 20)

  def reset_position(self, x: int = ...):
    self.goto(x = self.initial_x, y = 0)
