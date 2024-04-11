from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  # Move distance for each of the cars on refresh
MOVE_INCREMENT = 5    # How much the move_distance increments per level up (HIGHER LEVEL = HIGHER CAR SPEED.)
FINISH_LINE_Y =  280 # Y co-ordinate where finish line is located.
DIRECTIONS = ("forward", "backward")

class CarManager:

    def __init__(self):     # Constructor for "Car" objects (used to generate object instances via 'for' loop.)
        self.all_cars = []  # Creating a list which adds cars to it as they spawn.
        self.car_speed = STARTING_MOVE_DISTANCE     #setting inital car speed

    # CREATING CARS FUNCTION:
    def create_cars(self):

        random_chance = r.randint(1, 6)     # Creating a random spawn chance

        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)     #  No changes to width, stretches the length by 2.
            new_car.penup()
            new_car.color(r.choice(COLORS))  # Chooses random color for each car object.
            random_y = r.randint(-250, 250)     # Screen is 600 pixels height, leaving 50px for starting and end point where cars cannot appear.
            new_car.goto(300, random_y)     
            self.all_cars.append(new_car)      # Adding new car object instance to the car list.

    # Granting the cars movement:
    def move_cars(self):
       for car in self.all_cars:
           car.backward(self.car_speed)
       
    # Detecting when a level has been completed:
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    # ONCE FINISHED LEVEL DETECTED (REACHED FINISH_LINE_Y POSITION)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT    # Increases car speed by increment each time level up occurs