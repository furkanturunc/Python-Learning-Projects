from turtle import Turtle

FONT = ('Courier', 24, 'normal')
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0

        # data file keeps highest score even if the program is rerun
        # initially we put 0 to file if it does not exist
        try:
            with open("data.txt", "r") as data:
                self.highest_score = int(data.read())
        except FileNotFoundError:
            with open("data.txt", "w") as data:
                data.write("0")
            self.highest_score = 0

        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highest Score: {self.highest_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highest_score}")

        self.score = 0
        self.update_scoreboard()