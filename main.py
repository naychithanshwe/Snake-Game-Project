# pseudocode
# Step 1: Create a snake
# Step 2: Make the snake move forward
# Step 3: Make the snake controlled by arrow keys
# Step 4: collision detection with food
# Step 5: Scoreboard
# step 6: collision detection with wall
# step 7: collision with tail

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# create screen
screen = Screen()
screen.setup(600, 600)  # screen size
screen.title("Snake Game")
screen.bgcolor("Black")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.tracer()  # to remove trace of animation

# control the snake direction with arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # food collision detection
    if snake.head.distance(food) < 20:
        food.refresh()

screen.exitonclick()
