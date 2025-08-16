from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create left and right paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# create the ball
ball = Ball()

# create scoreboard
scoreboard = Scoreboard()

# event listener for both paddles movement
screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

is_game_on = True

while is_game_on:
    # screen is refreshed continuously
    screen.update()
    # move the ball
    ball.move()

    # ball slowness increases until goal
    time.sleep(ball.slowness)

    # when the ball hits the wall, it should bounce in y direction
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # if the ball hits a paddle, it should bounce in x direction
    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50) and abs(ball.xcor()) > 320:
        ball.bounce_x()

    # when the ball exceeds some x point, then it is a goal
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()