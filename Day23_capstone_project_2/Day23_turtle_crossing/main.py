import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

success = [-205, -130, -55, 20, 95, 170, 245]
count_list = []
count = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#creating the turtle
player = Player()

#dealing with cars
car_r1 = CarManager(x=0, y= -225)
car_r2 = CarManager(x=50,y=-150)
car_r3 = CarManager(x= -150, y= -75)
car_r4 = CarManager(x=-250, y= 0)
car_r5 = CarManager(x=150, y= 75)
car_r6 = CarManager(x=150, y= 150)
car_r7 = CarManager(x=200, y= 225)

#display score
display = Scoreboard()

#control player
screen.listen()
screen.onkey(fun=player.move, key="space")
game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()
    car_r1.move_car()
    car_r2.move_car()
    car_r3.move_car()
    car_r4.move_car()
    car_r5.move_car()
    car_r6.move_car()
    car_r7.move_car()

    #detecting collision and declare game over
    for cars in car_r1.car_list:
        if player.distance(cars) < 10:
            game_is_on = False
            display.game_over()


    for cars in car_r2.car_list:
        if player.distance(cars) < 10:
            game_is_on = False
            display.game_over()


    for cars in car_r3.car_list:
        if player.distance(cars) < 10:
            game_is_on = False
            display.game_over()

    for cars in car_r4.car_list:
        if player.distance(cars) < 10:
            game_is_on = False
            display.game_over()


    for cars in car_r5.car_list:
        if player.distance(cars) < 10:
            game_is_on = False
            display.game_over()


    for cars in car_r6.car_list:
        if player.distance(cars) < 10:
            game_is_on = False
            display.game_over()


    for cars in car_r7.car_list:
        if player.distance(cars) < 10:
            game_is_on = False
            display.game_over()

    #adding score and declare winner
    for pos in success:
        if player.ycor() == pos:
            show_score = success.index(pos)+1
            display.add_score(show_score)

        if player.ycor() > 245:
            game_is_on = False
            display.won()



screen.exitonclick()






