from turtle import Screen, Turtle
import random
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(False)
screen.listen()
is_game_on = True

paddle_left = Paddle("LEFT")
paddle_right = Paddle("RIGHT")
ball = Ball()

screen.onkey(key="Up", fun=paddle_left.up)
screen.onkey(key="Down", fun=paddle_left.down)
screen.onkey(key="w", fun=paddle_right.up)
screen.onkey(key="s", fun=paddle_right.down)

scoreboard = Scoreboard()

while is_game_on:
    ball.move_ball()

    if ball.distance(paddle_right) < 50 and paddle_right.xcor() > 365 or ball.distance(
            paddle_left) < 50 and paddle_left.xcor() < -365:
        ball.reverse_x_dir()

    if ball.xcor() > 380:
        scoreboard.set_score_of_right_player()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.set_score_of_left_player()
        ball.reset_position()

    if scoreboard.score_of_left == 10 or scoreboard.score_of_right == 10:
        scoreboard.print_game_over_message()
        is_game_on = False

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
