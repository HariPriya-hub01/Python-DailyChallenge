from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple" , "brown"]

class CarManager(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.new_x = x
        self.new_y = y
        self.car_list = []
        self.game_on = True
        self.create_cars()

    def create_cars(self):
         for i in range(1,10):
             new = Turtle()
             #new.hideturtle()
             new.shape("square")
             new.penup()
             new.shapesize(stretch_wid=0.8, stretch_len=2)
             new.color(random.choice(COLORS))
             new.goto(self.new_x, self.new_y)
             self.car_list.append(new)
             self.new_x += random.randint(70,200)
         self.hideturtle()
         self.move_car()

    def move_car(self):
        #while self.game_on:
        for j in range(0, len(self.car_list)):
            #print("in the move loop: ",j)
            move_x = self.car_list[j].xcor() - 20
            #print(move_x)
            move_y = self.car_list[j].ycor()
            #print(move_y)
            if move_x < -300:
                move_x = 300
            self.car_list[j].goto(x=move_x, y=move_y)


