from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(0.5)
        self.penup()
        self.display_food()


    def display_food(self):
        x_position = random.randint(-330,330)
        y_position = random.randint(-330,330)
        
        self.goto(x=x_position, y=y_position)