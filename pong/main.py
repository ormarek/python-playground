from turtle import Screen
from pong.paddle import Paddle
from pong.ball import Ball

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle_1 = Paddle(-390)
paddle_2 = Paddle(380)
ball = Ball()

screen.listen()
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")
screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")

game_is_on = True
while game_is_on:
  screen.update()
  ball.move()

  if ball.ycor() > 290 or ball.ycor() < -280:
    ball.wall_bounce()

  if (ball.xcor() > 360 and ball.xcor() < 370 and ball.distance(paddle_2) < 50) or (ball.xcor() < -370 and ball.xcor() > -380 and ball.distance(paddle_1) < 50):
    ball.paddle_bounce()

  if (ball.xcor() > 370 or ball.xcor() < -385):
    ball.reset_position()
    paddle_1.reset_position()
    paddle_2.reset_position()

screen.exitonclick()
