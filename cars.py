from turtle import Turtle
import random


COLORS = ["yellow", 'green', 'pink', 'red', 'blue', 'magenta', 'violet', 'orange']


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        # cars list contains all turtle cars objects
        self.cars = []
        self.hideturtle()

    def create(self):
        # in order for many cars to not be created, condition is set
        # condition is: two randomly generated numbers are even
        if random.randint(1, 2) % 2 != 0 and random.randint(1, 2) % 2 != 0:
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(300, random.randint(-220, 240))
            self.cars.append(car)

    # moves all cars from the list by random distance
    def move(self):
        for car in self.cars:
            car.forward(10)

    # checks if any of the cars hit turtle
    def hit_the_object(self, object):
        for car in self.cars:
            if car.distance(object) < 40 and abs(car.ycor()-object.ycor())<20:
                return True
