from turtle import Turtle
import time as t


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("./high_score_record.txt") as high_score:
                content = high_score.read()
        except FileNotFoundError:
            with open("./high_score_record.txt", "w") as high_score:
                content = high_score.write("0")
                self.high_score = 0
        else:
            self.high_score = round(float(content), 1)
        self.create_score()
        self.level = 0

    def create_score(self):
        """Creates and displays the score on the screen."""
        self.clear()
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0, 310)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", font=("Sans", 20, "normal"), align="center")

    def add_1(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./high_score_record.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")
        self.create_score()

    def add_half(self):
        self.clear()
        self.score += 0.5
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./high_score_record.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")
                print(self.high_score)
        self.create_score()

    def game_over(self, sentence):
        self.color("red")
        self.goto(0, 30)
        self.write(f"GAME OVER!", font=("Sans", 30, "normal"), align="center")
        self.goto(0, 10)
        self.write(f"{sentence}", font=("Sans", 10, "normal"), align="center")

    def level_up(self):
        self.color("green")
        self.goto(0, 30)
        self.level += 1
        self.write(f"LEVEL {self.level}", font=("Arial", 50, "normal"), align="center")

    def lets_see(self, head):
        self.color("green")
        if head < 220:
            self.goto(0, head + 30)
        else:
            self.goto(0, head - 40)

        self.write(f"Very well! Let's see how far you can get.", font=("Arial", 30, "normal"), align="center")

    def regressive_3(self):
        self.color("green")
        self.goto(0, 20)
        self.write("3", font=("Arial", 50, "normal"), align="center")

    def regressive_2(self):
        self.color("green")
        self.goto(0, 20)
        self.write("2", font=("Arial", 50, "normal"), align="center")

    def regressive_1(self):
        self.color("green")
        self.goto(0, 20)
        self.write("1", font=("Arial", 50, "normal"), align="center")

    def go(self):
        self.color("green")
        self.goto(0, 20)
        self.write("GO!", font=("Arial", 50, "normal"), align="center")

    def catch_the_food(self):
        self.goto(0, 20)
        self.write("Avoid half points by catching\n   the food while it's moving!", font=("Sacramento Regular", 20,
                                                                                        "normal"), align="center")

    def restart(self):
        self.score = 0
        self.level = 0
        self.create_score()

