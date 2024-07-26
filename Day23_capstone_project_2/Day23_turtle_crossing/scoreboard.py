from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.game_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color("black")
        self.write(arg=f"Score: {self.game_score}", align="center", font=FONT)

    def add_score(self, show_score):
        self.clear()
        self.write(arg=f"Score: {show_score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", align="center", font=("Courier", 24, "bold"))

    def won(self):
        self.goto(0, 0)
        self.write(arg="YOU WON!", align="center", font= ("Courier", 24, "bold"))



