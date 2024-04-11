from turtle import Turtle

START_POSITION = (0, -280)  # Start position for the turtle 
MOVE_DISTANCE = 10      # Movement increment per 'forward' move
FINISH_LINE_Y = 280     # Where the finish line is located on the screen. Once finsih line is touched by turtle, increment level count and reset player to the start position.

class Player(Turtle):

    def __init__(self):
        super().__init__()          # Inheriting superclass (turtle attributes + methods)
        self.shape("turtle")
        self.color("White")
        self.penup()                # Removes trail for travel
        self.go_to_start()   
        self.setheading(90)         # Turns turtle to face North. (0 = facing east)

    # Moving forward by 'move distance' each key listen.
    def Go_forward(self):
        self.forward(MOVE_DISTANCE)     


    # Brings player to starting position (at bottom of road). This occurs once level is complete OR gameover.
    def go_to_start(self):
        self.goto(START_POSITION)

    # Detecting when the player is over the finshing line Y co-ordinates:
    def is_at_finish_line(self):    
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False