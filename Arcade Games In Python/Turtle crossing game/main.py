# Imports 
from turtle import Turtle, Screen
from time import sleep
from player import Player
from car import CarManager
from scoreboard import Scoreboard

# Setting up GUI:
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Turtle crossing!")
screen.tracer(0)        # removes tracer (loading animation for movements).

player = Player()       # creates player object + starting co-ords for object.
scoreboard = Scoreboard()   # creating object for scoreboard.
car_manager = CarManager()

# Turtle movement:
screen.listen()
screen.onkey(player.Go_forward, "w")

# SETTING UP WHILE LOOP FOR GAME TO RUN:
game_is_on = True

while game_is_on:
    sleep(.1)       
    screen.update()        # Refreshes and updates screen every .1 secs 

    car_manager.create_cars()       # Creates a new car on each refresh of game loop.
    car_manager.move_cars()         # Generates movement for the created cars.


    # DETECTS CAR COLLISION:
    for car in car_manager.all_cars:
        if car.distance(player) < 30:       # If distance between the car and the player is less than 20 (collision occured)
            game_is_on = False      # Ends while loop (game ends.)
            scoreboard.game_over()  # Calls 'gameover' func.

    # DETECT SUCCESSFUL CROOSING (PASSING FINISH LINE, NEXT LEVEL)
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()     # Calls function to increase level.


screen.exitonclick()    # Enables window screen to be displayed (game ends once the screen 'close' is clicked.)
