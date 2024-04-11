from turtle import Turtle

class Ball(Turtle):     # Setting up ball class.

    def __init__(self):         # Creating constructor for object creation of ball.
        super().__init__()      # Inherit from superclass ("Turtle" library)

        self.color("White")     # Sets ball's color
        self.shape("circle")
        self.penup()        # Penup removes path trail when moving.
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1       # Setting initial ball speed.

    def move(self):
        ball_new_x = self.xcor() + self.xmove   # Travels by specified amount of pixels along "x coord".
        ball_new_y = self.ycor() + self.ymove   # Travels by specified amount of pixels along "y coord".
        self.goto(ball_new_x, ball_new_y)

    def bounce_y(self):
        self.ymove *= -1       # Multiplies by minus one (shifts from positive diagonal motion [UP] to negative [DOWN])
                                # Overwrites y_move variable until another collision occurs to switch balls motion to
                                # React to collision and travel freely. 

    # FLIPS TRAJECTORY ONCE BALL COLLIDED WITH PADDLES:
    def bounce_x(self):
        self.xmove *= -1    # Multiplying "x" co-ordinate by -1 flips the trajectory from negative (down)
                            # Back to positive/
        self.move_speed *= 0.9  # Reduces ball speed number = increases speed of the ball as paddle collisions build up.

    # RESETTING BALL ONCE MISSED AND POINT CONCEDED BY A PLAYER:
    def reset_ball_pos(self):   # Brings the ball back to the starting position of new game (center.)
        self.goto(0, 0)
        self.move_speed = 0.1    # Sets ball speed back to normal once position is reset.
        self.bounce_x()  # Continues ball movement from start travelling towards the opponent who scored.