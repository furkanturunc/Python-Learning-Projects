from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.reset_position()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def is_achieved(self):
        if self.ycor() > 280:
            return True
        return False
