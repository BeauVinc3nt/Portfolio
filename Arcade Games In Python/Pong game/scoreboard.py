from turtle import Turtle

# Setting re-usable format vals:
SCORE_FONT = "Courier", 80, "normal"
SCORE_ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):     # Creating constructor for Scoreboard object(s)
        super().__init__()
        self.color("White")     # Scoreboard tracker is "White" to follow theme and show scoreboard clearly.
        self.penup()            # Removes trail for relocating "player scores":
        self.hideturtle()

        # SETTING PLAYER 1 AND 2 SCORES (TO BE INCREMENTED)
        self.P1_score = 0   
        self.P2_score = 0
        self.update_scoreboard()    # Function call to update each player's scoreboard.

    def update_scoreboard(self):
        self.clear()             # Calls "clear" function to clear and overwrite score count as it changes.

        # PLAYER 1 SCORE COUNT POSITIONING:
        self.goto(-100, 180)
        self.write(self.P1_score, align=(SCORE_ALIGN), font=(SCORE_FONT))

        # PLAYER 2 SCORE COUNT POSITIONING:
        self.goto(100, 180)
        self.write(self.P2_score, align=(SCORE_ALIGN), font=(SCORE_FONT))

    # Incrementing Player 1 + Player 2's score by one & updating their score
    def P1_point(self):
        self.P1_score += 1          
        self.update_scoreboard()    

    def P2_point(self):
        self.P2_score += 1          
        self.update_scoreboard()           