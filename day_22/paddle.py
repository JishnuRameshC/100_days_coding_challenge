from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.goto((position))
        self.shapesize(5,1)

    def up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(),new_y)

