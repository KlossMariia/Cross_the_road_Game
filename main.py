from little_turtle import LittleTurtle
from turtle import Screen, Turtle
import time
from cars import Cars
from scoreboard import Score

# creating screen
screen = Screen()
screen.title("Cross the Road Game")
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)
# creaing a turtle
turtle = LittleTurtle()
screen.listen()
# setting keyboard control
screen.onkey(key="Up", fun=turtle.up)
screen.onkey(key="Down", fun=turtle.down)
# creating cars
car = Cars()
score = Score()
game_is_on = True
while game_is_on:
    time.sleep(score.speed)
    screen.update()
    score.create_writing()
    if car.hit_the_object(turtle):
        game_is_on = False
        score.game_over()
    # user wins a round if crosses the road
    # after each round car speed increases
    if turtle.ycor() > 280:
        score.up()
        turtle.reset()
        score.speed_up()
    # creates cars and moves them by random distance
    car.create()
    car.move()
screen.exitonclick()

