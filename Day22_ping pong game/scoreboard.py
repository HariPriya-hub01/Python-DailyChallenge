from turtle import Turtle

class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(f"Score\n  {self.score}", align="center", font=("courier", 20, "bold"))

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score\n  {self.score}", align="center",font=("courier", 20, "bold"))