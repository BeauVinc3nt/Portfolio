from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()      # Inherit traits from superclass (turtle).
        self.level = 1          # Initial level on game load up.
        self.hideturtle()       # Hides turtle so that moving from origin to position's trace doesn't show.
        self.penup()
        self.goto(-330, 240)        # Sets position of scoreboard on the screen.
        self.color("White")
        self.update_scoreboard()


# CALLING SCOREBOARD UPDATE FUNCTION ONCE CURRENT LEVEL IS COMPLETED.
    def update_scoreboard(self):
        self.clear()    # Clears initial score.
        self.write(f"Level: {self.level}", align = "left", font = FONT) # Rewriting new score in specified format.

    def increase_level(self):
        self.level += 1             # Incrementing level count by one.
        self.update_scoreboard()    # Call update func to clear and overwrite new level once level complete.
    
    # Setting up gameover message and position reset.
    def game_over(self):
        self.goto(0, 0)     # Resets axis to starting default positiom.
        self.write(f"GAME OVER!", align = "center", font = FONT)
        self.goto(0, -55)
        self.write(f"CLICK THE SCREEN TO RESTART.", align = "center", font = ("Courier", 15, "normal"))