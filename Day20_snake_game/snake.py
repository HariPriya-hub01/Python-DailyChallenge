from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_list = []
        self.places = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()


    def create_snake(self):
        # for loop for starting position
        for pos in self.places:
            self.add_segment(position=pos)

    def add_segment(self, position):
        new = Turtle(shape="square")
        new.pencolor("white")
        new.penup()
        new.fillcolor("cyan")
        new.goto(position)
        self.snake_list.append(new)

    def grow(self):
        self.add_segment(self.snake_list[-1].position())

    def Move(self):
        for snake in range(len(self.snake_list)-1, 0, -1):
            new_x = self.snake_list[snake - 1].xcor()
            new_y = self.snake_list[snake - 1].ycor()
            self.snake_list[snake].goto(new_x, new_y)
        self.snake_list[0].forward(20)


    def up(self):
        if self.snake_list[0].heading() != 270:
            self.snake_list[0].setheading(90)
    def down(self):
        if self.snake_list[0].heading() != 90:
            self.snake_list[0].setheading(270)
    def right(self):
        if self.snake_list[0].heading() != 180:
            self.snake_list[0].setheading(0)
    def left(self):
        if self.snake_list[0].heading() != 0:
            self.snake_list[0].setheading(180)

