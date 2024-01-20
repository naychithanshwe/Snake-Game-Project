import random
from turtle import Turtle, Screen
FOOD_SHAPE = "circle"
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.color("White")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_x = random.randint(-260,260)
        new_y = random.randint(-260,260)
        self.goto(new_x,new_y)

