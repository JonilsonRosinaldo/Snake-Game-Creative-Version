from turtle import Turtle
from random import randint, choice


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        self.shape("turtle")
        self.color(choice(["orange", "yellow", "pink", "purple", "blue", "green", "grey", "brown"]))
        self.pu()
        self.shapesize(0.5)
        self.goto(randint(-330, 330), randint(-330, 310))

    def food_eaten(self):
        self.clear()
        self.create_food()

    def test(self):
        list = [1, 2, 3, 4, 5, 6]
        return list

    def move(self):
        if -330 < self.xcor() < 330 and 330 > self.ycor() > -325:
            choice([self.right((randint(0, 90))), self.left((randint(0, 90)))])
            self.forward(4)
