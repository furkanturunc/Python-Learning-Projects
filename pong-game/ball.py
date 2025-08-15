from turtle import Turtle

INITIAL_SLOWNESS = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.width(20)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.slowness = INITIAL_SLOWNESS

    def move(self):
        self.penup()
        xcor = self.xcor() + self.x_move
        ycor = self.ycor() + self.y_move
        self.goto(xcor, ycor)

    def bounce_x(self):
        self.x_move *= -1
        self.slowness *= 0.9

    def bounce_y(self):
        self.y_move *= -1
        self.slowness *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.slowness = INITIAL_SLOWNESS




