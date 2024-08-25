import time
from turtle import Screen
from paddle import Paddle
from Ball import Ball
from Brickes import Bricks

l = ['Akash', 'Deependra', 'Dindon', 'yoske', 'Moti', 'Neli']


def create_bricks(my_list, ships_fleet):
    k = -250
    p = 200
    x = -250
    y = 55
    for i in range(0, 6):
        ships_fleet[i].goto(k, p)
        k += 100

    for i in range(0, 6):
        my_list[i].goto(x, y)
        print(x, y)
        x += 100
    return ships_fleet


screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

# paddle  Brickes Ball classes
ball = Ball()
pad = Paddle()

ships_fleet = [Bricks() for _ in l]
my_list = [Bricks() for _ in l]
create_bricks(ships_fleet, my_list)

# button-click events
screen.onkey(key="Right", fun=pad.move_right)
screen.onkey(key="Left", fun=pad.move_left)

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    for my_list_ship_number in range(0, 6):
        if ball.distance(my_list[my_list_ship_number]) < 30:
            my_list[my_list_ship_number].goto(1111,1111)
            ball.bounce_y()
        if ball.distance((ships_fleet[my_list_ship_number])) < 30:
            ships_fleet[my_list_ship_number].goto(1111,1111)
            ball.bounce_y()

    if ball.xcor() > 260 or ball.xcor() < -270:
        ball.bounce_x()

    if ball.distance(pad) < 33:
        ball.bounce_y()

    if ball.ycor() > 240:
        ball.bounce_y()
screen.exitonclick()
