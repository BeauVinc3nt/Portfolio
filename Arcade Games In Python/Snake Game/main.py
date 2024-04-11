# Library imports
from turtle import Screen
from time import sleep
from Snake_class import Snake    # External file imports from project
from SnakeFood_class import SnakeFood
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)    # tracer(0) = no animation delay

# Initializing objects from their classes:
snake = Snake() 
food = SnakeFood()
scoreboard = Scoreboard()

game_is_on = True   # Setting condition to keep the game running.

# DETECTING SNAKE MOVEMENT INPUTS:
screen.listen()     # Checking for inputs for movement
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    sleep(0.1)      # whilst game is running, screen updates every 0.1 secs.

    snake.move()    # calls method to move snake.

    # DETECTING COLLISIONS WITH THE FOOD:
    if snake.head.distance(food) < 15:      # 10 = collision point (eaten when 1/4 of a turtle's length away from the food)
        print("Nom nom nom.")   # Registers in console for each food eaten.
        food.refresh()      # Calls refresh function
        snake.extend()  # Increments length of snake by 1.
        scoreboard.increase_score() 

    # DETECTING COLLISIION WITH THE WALL (X or Y position exceeds the screen width):
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()  # Displays "game over" screen.
        snake.reset()       # Calling reset method to set snake to default size + score.

    # DETECTING COLLISION WITH TAIL:
    for segment in snake.segments:
        if segment == snake.head:   # Disregards the head collision as this would happen every frame 
            pass
        elif snake.head.distance(segment) < 15:
            scoreboard.reset()

screen.exitonclick()    # Enables the GUI window to be closed once window clicked.



