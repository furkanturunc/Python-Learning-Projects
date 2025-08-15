from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.width(20)
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.penup()
        self.goto(coordinates[0], coordinates[1])

    def up(self):
        x = self.xcor()
        y = self.ycor() + 20
        self.goto(x, y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 20
        self.goto(x, y)