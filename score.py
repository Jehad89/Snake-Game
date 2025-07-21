from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=320)
        self.hideturtle()
        self.result()


    def result(self):
        self.clear()
        self.write(f"Score: {self.score}", font=('courier',18,'normal'), align='center')

    def add_point(self):
        self.score += 1
        self.result()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.screen.bgcolor('darkred')
        self.write(f"_______________Game Over_________________\n\nYour score is: {self.score}", font=('courier',16,'bold'),align='center')