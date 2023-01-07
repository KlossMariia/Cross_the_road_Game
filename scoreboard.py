from turtle import Turtle


# keeps track of score
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-15, 270)
        self.speed("fastest")
        self.create_writing()
        self.speed = 0.1

    def create_writing(self):
        self.clear()
        arg = f"Level: {self.score}"
        self.write(arg, False, "center", ('Times New Roman', 20, 'normal'))

    # shows fame over message
    def game_over(self):
        self.goto(-10, 0)
        self.write("GAME OVER", False, "center", ('Times New Roman', 40, 'normal'))

    # adds a score
    def up(self):
        self.score += 1

    # decreases time of sleep, so cars move faster
    def speed_up(self):
        self.speed *= 0.8

