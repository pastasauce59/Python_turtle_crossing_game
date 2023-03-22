import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Generates new car on every 6th time of game loop
    if loop % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()
    
    #Detect player collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False

    #Detect player crossing finish line
    if player.is_at_finish_line():
        player.set_player()
        car_manager.increase_speed()
    
    #Increase loop count with every loop iteration
    loop += 1
screen.exitonclick()