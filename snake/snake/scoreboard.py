from turtle import Turtle

TEXT_ALIGN="center"
FONT=("Arial", 24, "normal")

class Scoreboard(Turtle):
  def __init__(self) -> None:
    super().__init__()
    self.score = 0
    self.hideturtle()
    self.penup()
    self.color("white")
    self.goto(0, 270)
    self.write_score()

  def game_over(self):
    self.goto(0, 0)
    self.write(f"Game over!", align=TEXT_ALIGN, font=FONT)

  def write_score(self):
    self.clear()
    self.write(f"Score: {self.score}",  align=TEXT_ALIGN, font=FONT)

  def add_point(self):
    self.score += 1
    self.write_score()
