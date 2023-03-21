import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = []

screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Generates new car on every 6th time of game loop
    if loop % 6 == 0:
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:
        #Detects car collision with player
        if player.distance(car) < 35:
            game_is_on = False
        else:
        #Otherwise makes every car in 'cars' list move forward across the screen
            car.move()
    
    #Increase loop count with every loop iteration
    loop += 1
screen.exitonclick()