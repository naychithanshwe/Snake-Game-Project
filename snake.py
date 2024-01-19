from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.move()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("White")
            new_segment.penup()  # to remove the drawing line
            new_segment.goto(position)  # positioning the snake in the middle using coordinates
            self.segments.append(new_segment)

    def move(self):
        for segment_number in range(len(self.segments)-1,0,-1): # move all the snake segments in line
            new_x = self.segments[segment_number-1].xcor()
            new_y = self.segments[segment_number-1].ycor()
            self.segments[segment_number].goto(new_x,new_y)

        self.head.forward(20)


