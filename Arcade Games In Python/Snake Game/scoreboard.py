from turtle import Turtle
import datetime as dt       # Used to save the date and time of high score entries for the game.

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

FullTimeNow = dt.datetime.now()
Formatted_Current_DateTime = FullTimeNow.strftime("%d/%m/%Y, %H:%M:%S")   # Storing datetime as format: "date + time"

class Scoreboard(Turtle):   # Inherits properties from "Turtle" super class

    def __init__(self):     # Creating constructor for inherited "Turtle" class
        super().__init__()
        self.score = 0      # Setting initial score value

        # OPENING HIGHSCORE FILE & READING FILE CONTENTS:
        with open("high_score_log.txt", mode = "r") as highscore_data:  
             self.highscore = int(highscore_data.read())  # Saving object's highscore attribute as file contents.
        
        self.color("White")
        self.penup()        # Removing turtle trace for moving text to top of page
        self.goto(0, 230)   # Positioning text
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)    # Text properties 
        self.hideturtle()   # Hiding the turtle arrow shape from the center of the text
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align = ALIGNMENT, font = FONT) # Setting display for UI of High Score contents

    def increase_score(self):       # Increments score by 1 each time.
        self.score += 1
        self.clear()                # Clears the initial score
        self.update_scoreboard()

# Calls reset function - checks if score surpasses highscore ->IF TRUE, update highscore + reset score once game over.
    def reset(self):
        if self.score > self.highscore: # If score's greater than the highscore, set new highscore value.
            self.highscore = self.score
            with open("high_score_log.txt", mode = "w") as highscore_data:  # Setting file mode to "write to create new contents and overwrite previous data values.
                highscore_data.write(f"{self.highscore}\n")

        self.score = 0  # Reset score to 0 (reset carried out.)
        self.update_scoreboard()    # Once reset, call update function.



        