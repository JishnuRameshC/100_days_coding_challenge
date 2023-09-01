from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]



    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def resets(self):
        for seg in self.segments:
            seg.goto(1000,100)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]




    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg_numb in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_numb - 1].xcor()
            new_y = self.segments[seg_numb - 1].ycor()
            self.segments[seg_numb].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        if  self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if  self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if  self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if  self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    
