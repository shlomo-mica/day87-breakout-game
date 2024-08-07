import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = turtle.Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-260, 260)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.bk(STARTING_MOVE_DISTANCE)


window = turtle.Screen()
window.title('Breakout_ver1')

ball = turtle
ball.shape('circle')
ball.color('red')
window.bgcolor('black')
ball.penup()

ship = turtle.Turtle()
ship.shape('turtle')
ship.shapesize(13, 13)
ship.forward(322)
ship.setposition(222,100)
ship.color('green')
X_090 = window.window_width() / 2
Y_090 = window.window_height() / 2
DX = 2
x = random.randrange(0, 90)
random_angel = random.choice([-2, +2])
RND_X = random.randrange(-4, +4)
RND_Y = random.randrange(-4, +4)
ball_start_position = ball.setposition(RND_X, -316)


def hit_one():
    while True:
        if ball.ycor() < Y_090:
            ball.setposition(ball.xcor() - 2, ball.ycor() + 2)
            print(ball.pos())
        else:
            while True:
                ball.setposition(ball.xcor() - 2, ball.ycor() - 2)
                if ball.xcor() < -X_090:
                    while True:
                        ball.setposition(ball.xcor() + 2, ball.ycor() - 2)
                        if ball.ycor() < -Y_090:
                            while True:
                                ball.setposition(ball.xcor() + 2, ball.ycor() + 2)
                                if ball.xcor() < X_090:
                                    return 2


def first_angle_hit2():
    list1 = [2, 2], [-2, 2]
    random_direction = random.choice(list1)
    dx = random_direction[0]
    dy = random_direction[1]
    ball.setposition(ball.xcor() + dx, ball.ycor() + dy)
    return


def bottom():
    ball.speed(3)
    all_directions(-2, 2)


# false--left    true--right


def all_directions(x, y):
    while True:
        print(x, y)
        ball.setposition(ball.xcor() + x, ball.ycor() + y)
        print(ball.xcor(), ball.ycor())
        if X_090 > ball.xcor() > -X_090:
            print("e")
        else:
            while True:
                ball.setposition(ball.xcor() - x, ball.ycor() + y)
                if ball.ycor() > Y_090:
                    while True:
                        ball.setposition(ball.xcor() - x, ball.ycor() - y)
                        print("start down")
                        if ball.xcor() > X_090 or ball.xcor() < -X_090:
                            print("bottom111", ball.xcor(), ball.ycor(), x, y)

                            while True:
                                ball.setposition(ball.xcor() + x, ball.ycor() - y)
                                print("bottom222", ball.xcor(), ball.ycor(), x, y)
                                if ball.ycor() < -Y_090 + 22:
                                    return 1

                                # all_directions(dx,dy)


list1 = [2, 2], [-2, 2]
random_direction = random.choice(list1)
dx = random_direction[0]
dy = random_direction[1]

while True:
    if all_directions(dx, dy) == 1:
        bottom()

turtle.mainloop()
