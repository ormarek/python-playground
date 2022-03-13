from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
  def __init__(self) -> None:
    self.segments = []
    self.init_snake()
    self.head = self.segments[0]

  def init_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)

  def move(self):
    for segment in range(len(self.segments) - 1, 0, -1):
      previous_segment = self.segments[segment - 1]
      self.segments[segment].goto(previous_segment.position())
    self.head.forward(MOVE_DISTANCE)

  def add_segment(self, position):
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    self.segments.append(segment)

  def extend(self):
    self.add_segment(self.segments[-1].position())

  def turn_right(self):
    if (self.head.heading() != 180):
      self.head.setheading(0)

  def turn_up(self):
    if (self.head.heading() != 270):
      self.head.setheading(90)

  def turn_left(self):
    if (self.head.heading() != 0):
      self.head.setheading(180)

  def turn_down(self):
    if (self.head.heading() != 90):
      self.head.setheading(270)
