from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.fillcolor("yellow")
        self.penup()
        self.shapesize(0.5,0.5)
        self.food_rand()

    def food_rand(self):
        x_pos = random.randint(-280,280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos,y_pos)


