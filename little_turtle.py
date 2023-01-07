from turtle import Turtle

# this class is responsible for creating a turtle
class LittleTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.goto(0, -260)

    def up(self):
        self.forward(10)

    def down(self):
        if self.ycor() > -280:
            self.back(10)

    # sends turtle back to its starting position
    def reset(self):
        self.goto(0, -260)
