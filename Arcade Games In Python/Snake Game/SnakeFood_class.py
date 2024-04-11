from turtle import Turtle, colormode
import random as r   # Used for random color generation
from random import randint # Used to generate random position for snake food instances
 

# CHOOSING RANDOM COLOR FOR FOOD EACH TIME:
Turtle_colors = ["AliceBlue","Coral","DarkGoldenrod","blue","cyan","darkorchid","BlanchedAlmond",
                "Brown", "aquamarine", "burlywood"]


class SnakeFood(Turtle):

   def __init__(self):
      super().__init__()        # Inherit from superclass (Turtle) methods and attributes.
      self.shape("circle") # Specifying food shape
      self.penup()  # Removes pen tracing for position switching.
      self.shapesize(stretch_len = 0.5, stretch_wid=0.5)    # Modifying turtle size from (40, 40) to (20, 20)
      self.speed(5)     # Fastest speed no animation
      self.refresh()    # Calls refresh function:
      

   def refresh(self):
      Random_color = r.choice(Turtle_colors)
      self.color(Random_color) # Choosing random color for snake food (re-assigns color each refresh).

      # SETTING RANDOM X AND Y CO-ORDS FOR FOOD:
      random_x_pos = r.randint(-280, 280)
      random_y_pos = r.randint(-280, 280)
      self.goto(random_x_pos, random_y_pos)     # Setting position of food to random co-ordinates (passing "x" and "y" values).
      