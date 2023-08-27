from turtle import Turtle


ALIGN =  'center'
FONT = ('Arial', 20, 'normal')


class Scorebord(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_scorebord()
         
    def update_scorebord(self):
        self.write(f"score = {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align= ALIGN, font= FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scorebord()
