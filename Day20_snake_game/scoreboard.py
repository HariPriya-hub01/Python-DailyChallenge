from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.inc = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y= 280)
        self.write(arg=f"Score : {self.inc} ", align='center')
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", align='center', font=("courier", 12,"bold"))

    def increase_score(self):
        self.inc += 1
        self.clear()
        self.write(arg=f"Score : {self.inc} ", align='center')



