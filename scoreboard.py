from turtle import Turtle, Screen
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score: {self.score}",False,"Center",("Courier",24,"normal"))


