from turtle import Screen
import time

from snake.food import Food
from snake.scoreboard import Scoreboard
from snake.snake import Snake

game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("Black")

screen.title("Snake")

#####################
scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")

while game_is_on:
  screen.update()
  time.sleep(0.5)
  snake.move()

  if snake.head.distance(food) < 10:
    food.set_pos()
    snake.extend()
    scoreboard.add_point()
  
  if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
    game_is_on = False
    scoreboard.game_over()
  
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()

screen.exitonclick()
