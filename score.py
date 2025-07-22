from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highscore()
        self.color('white')
        self.penup()
        self.goto(x=0, y=320)
        self.hideturtle()
        self.result()

    def get_highscore(self):
        with open("highscore.txt","r") as my_file:
            return (int(my_file.read()))

    def save_highscore(self):
        with open("highscore.txt","w") as my_file:
            my_file.write(str(self.highscore))

    def result(self):
        self.clear()
        self.write(f"Score: {self.score}    High score: {self.highscore}", font=('Arial',16,'bold'), align='center')

    def update_scoreboard(self):
        self.score += 1
        self.result()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.screen.bgcolor('darkred')
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.write(f"---------------Game Over---------------\n\nYour score is: {self.score}\n\nHigh Score: {self.highscore}", font=('courier',16,'bold'),align='center')