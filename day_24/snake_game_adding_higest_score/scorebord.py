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
        with open("high_score.txt") as file:
            self.highest_score = int(file.read())
        self.goto(0,270)
        self.update_scorebord()
         
    def update_scorebord(self):
        self.clear()
        self.write(f"score = {self.score} High score = {self.highest_score}", align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",align= ALIGN, font= FONT)


    def resets(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("high_score.txt", 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scorebord()
    
    def increase_score(self):
        self.score += 1
        self.update_scorebord()
