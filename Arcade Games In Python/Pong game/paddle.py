from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):           # Creating a constructor (for paddle objects to be made.)
        super().__init__()  # Inheriting from the superclass in Paddle class (Turtle) to use attributes and methods within Turtle on the "Paddle".
        self.shape("square")
        self.shapesize(5, 1)      # PARAMETERS FORMAT: (stretch width, stretch length)
        self.color("White")
        self.penup()   
        self.goto(position)         # Player 1's paddle moves to the left side of screen.

        # Taking keyboard keystrokes for up and down movements for paddles.
    def Go_up(self):
        new_ycor = self.ycor() + 20         # Moves '+10' up y-axis (up movement)
        self.goto(self.xcor(), new_ycor)    # Updates paddle Y-pos

        
    def Go_down(self):
        new_ycor = self.ycor() - 20     # Moves '-10' down y-axis (down movement)
        self.goto(self.xcor(), new_ycor) # Updates paddle X-pos

