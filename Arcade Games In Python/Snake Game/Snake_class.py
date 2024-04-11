from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20  # Turtle segment distance moved
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
CURRENT_SCORE = 0   # Keeps track of a score (how many foods have been eaten.)




# CREATING SNAKE CLASS:
class Snake(Turtle):
    def __init__(self):    # Constructor function - creating object instance
        self.segments = []  # Creating a list to increment amount of segments (dependant on food ate.)
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")  # Creating a turtle "segment"
        new_segment.color("white")
        new_segment.penup()             # Penup removes trace for turtles path travelled (removes trace lines)
        new_segment.goto(position)      
        self.segments.append(new_segment)   # Adding a new segment to the "segments" list 

    def reset(self):
            for seg in self.segments:
                seg.goto(1000, 1000)    # Sends the previous snake that's been reset to a co-ordinate outside the screen's view.

            self.segments.clear()   # All segments added to list of segments cleared.
            self.create_snake()     # CREATING SNAKE AGAIN (BACK AT CENTER)
            self.head = self.segments[0]        # Head is the first segment (index 0)


    def extend(self):   #Ffinding position of the last element (tail of the snake.)
        self.add_segment(self.segments[-1].position())  # Takes last element from the list (first element = index 0, last = index -1.) 

        # Adds a section to the snake's tail as it eats a piece of food.

    # DEFINING MOVEMENTS FOR THE SNAKE:
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):   # Parameter format: (start, stop, step)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

   