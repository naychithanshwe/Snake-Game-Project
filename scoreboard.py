from turtle import Turtle, Screen
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}",False,"Center",("Courier",24,"normal"))

    def scored(self):
        self.score +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, "Center", ("Courier", 24, "normal"))


