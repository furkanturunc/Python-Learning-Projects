from idlelib.zoomheight import set_window_geometry
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# setup screen size, background color, and title
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create snake and put onto screen
snake = Snake()
snake.head.speed(1000)

# create food
food = Food()

# create scoreboard
scoreboard = Scoreboard()

screen.listen()
is_game_on = True

screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key= "Down", fun=snake.down)
screen.onkey(key= "Left", fun=snake.left)
screen.onkey(key= "Right", fun=snake.right)

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check if snake eats food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # check if snake hits wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.reset()
        snake.reset()

    # check if snake head hits any of the other segments:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()





