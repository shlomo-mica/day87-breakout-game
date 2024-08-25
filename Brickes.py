from turtle import Turtle
import random

space_ship_colors = ['blue', 'yellow', 'red', 'green', 'orange', '#ff00ff']
w = random.randint(0, 5)
list22 = ['Akash', 'Deependra', 'Dindon', 'yoske', 'Moti', 'Neli']


class Bricks(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()

        self.create_bricks22()

    def create_bricks22(self):
        w = random.randint(0, 5)
        self.color(space_ship_colors[w])
    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(x=new_x, y=self.ycor())
