from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pos = position
        self.create(self.pos)
        #self.new_y = 0

    def create(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)



    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

