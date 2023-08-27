from turtle import Turtle

ALIGN =  'center'
FONT = ('Arial', 80, 'normal')


class Scorebord(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scorebord()

    def update_scorebord(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align=ALIGN, font=FONT)
        self.goto(100,200)
        self.write(self.r_score,align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scorebord()

    def r_point(self):
        self.r_score += 1
        self.update_scorebord()