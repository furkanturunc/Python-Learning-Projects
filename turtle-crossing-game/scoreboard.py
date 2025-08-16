from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-240, 270)
        self.hideturtle()
        self.level = 1
        self.level_slowness = 0.5
        self.update_level_info()

    def update_level_info(self):
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_level_info()
        self.level_slowness *= 0.9

    def game_over(self):
        self.clear()
        self.goto(-200, 270)
        self.write(arg=f"Game Over!", align="center", font=FONT)