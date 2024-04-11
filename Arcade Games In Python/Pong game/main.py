# Ping Pong arcade game:
import turtle as t
from turtle import Turtle, Screen
from paddle import Paddle   # Importing external files
from ball import Ball       #
from scoreboard import Scoreboard # 
from time import sleep

# SETTING UP SCREEN FOR GAME TO RUN:
screen = Screen()
screen.title("PingPong arcade game")
screen.bgcolor("black")
screen.setup(800, 600)      # Taking screen width & height parameters.
screen.tracer(0)    # Removing tracer removes animations time (for creating paddles.)  Screen update func required to display paddles and update keystrokes.

# SETTING CO-ORDINATES FOR PADDLE CLASSES, CREATING BALL + SCOREBOARD:
P1_paddle = Paddle((-350, 0))       
P2_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()


# TAKING MOVEMENT INPUTS (KEYSTROKES)
screen.listen()     # Listening for movements
screen.onkey(P1_paddle.Go_up, "w")
screen.onkey(P1_paddle.Go_down, "s")
screen.onkey(P2_paddle.Go_up, "Up")
screen.onkey(P2_paddle.Go_down, "Down")

# GAME RUNNING CONDITIONS (FOR TRACER [NO ANIMATION] & SETTING GAME OVER CONDITION.)
game_is_on = True

while game_is_on:
    sleep(ball.move_speed) # Screen refresh rate for ball
    screen.update() 
    ball.move()

    # Detecting collision with wall to result in ball bouncing off of wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()       # Call bounce function

    # Detect collision with right paddle:
    if ball.distance(P1_paddle) < 50 and ball.xcor() < -320 or ball.distance(P2_paddle) < 50 and ball.xcor() > 320:
       ball.bounce_x()

    # Detect when player 2 (RIGHT) paddle misses {P1 gains point}:
    if ball.xcor() > 380:
        ball.reset_ball_pos()   # Once detected as going past P2 paddle (not collided with paddle). This is registered as a scored point for the opponent. RESETS BALL TO START.
        scoreboard.P1_point()   # Func call to increment Player 1's scoreboard.


    # Detect when player 1 (LEFT) paddle misses {P2 gains point}:
    if ball.xcor() < -380:
        ball.reset_ball_pos()
        scoreboard.P2_point() # Func call to increment Player 2's scoreboard.


screen.exitonclick()    # Keeps window open until close clicked.



