from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.inc_x = 10
        self.inc_y = 10
        self.move_speed = 0.1
        #self.speed("slowest")


    def move(self):
        new_x = self.xcor() + self.inc_x
        new_y = self.ycor() + self.inc_y
        self.goto(new_x,new_y)

    def bounce(self):
        self.inc_y *= -1
        self.move()

    def paddle_bounce(self):
        self.move_speed *= 0.9
        self.inc_x *= -1
        self.move()

    def start_again(self):
        self.home()
        self.move_speed = 0.1
        self.paddle_bounce()




