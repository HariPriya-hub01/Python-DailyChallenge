import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_on = True
snake = Snake()
food = Food()
score = Scoreboard()
#time.sleep(0.1)
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.Move()
    screen.listen()
    screen.onkey(fun=snake.up,key="Up")
    screen.onkey(fun=snake.down,key="Down")
    screen.onkey(fun=snake.left,key="Left")
    screen.onkey(fun=snake.right,key="Right")

    #collision with food
    if snake.snake_list[0].distance(food) <15:
        food.food_rand()
        snake.grow()
        score.increase_score()

    #collision with wall
    if snake.snake_list[0].xcor() > 280 or snake.snake_list[0].xcor() < -280 or snake.snake_list[0].ycor() > 280 or snake.snake_list[0].ycor() < -280:
        game_on = False
        score.game_over()

    #collision with tail
    for segments in snake.snake_list[1:]:
        if snake.snake_list[0].distance(segments) < 15:
            game_on = False
            score.game_over()









screen.exitonclick()