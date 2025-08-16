from turtle import Screen
import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

# set up screen
screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)

# create scoreboard (level), player (turtle), car manager
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

# event listener for player movement
screen.listen()
screen.onkey(key="Up", fun=player.up)

is_game_on = True

while is_game_on:
    time.sleep(scoreboard.level_slowness)
    screen.update()
    car_manager.refresh()

    # if the player reaches the top position, level up (with a increased speed of cars)
    if player.is_achieved():
        player.reset_position()
        scoreboard.level_up()

    # if any car hits the player, game over
    if car_manager.hits(player):
        scoreboard.game_over()
        is_game_on = False

screen.exitonclick()