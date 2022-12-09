from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
paddle_right = Paddle((370, 0))
paddle_left = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_left) < 40 and ball.xcor() < -340 or ball.distance(paddle_right) < 40 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_points()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_points()

screen.exitonclick()
