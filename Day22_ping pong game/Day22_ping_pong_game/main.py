from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

#setting up the screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.tracer(0)

#creating the paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#dealing with the ball
ball = Ball()

#preparing the scoreboard
r_score = Score((100,200))
l_score = Score((-100,200))

#moving the paddles
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.down, key="s")

#updating the screen
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detecting collision with wall
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce()

    #detecting collision with paddle:
    if r_paddle.distance(ball) < 50 and ball.xcor() > 320 or l_paddle.distance(ball) < 50 and ball.xcor() < - 320:
        ball.speed()
        ball.paddle_bounce()

    #detecting ball miss
    if ball.xcor() > 340:
        ball.start_again()
        l_score.add_score()


    if ball.xcor() < -340:
        ball.start_again()
        r_score.add_score()

screen.exitonclick()
