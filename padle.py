from turtle import Turtle

STEP = 20


class Padle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + STEP
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - STEP
        self.goto(self.xcor(), new_y)
