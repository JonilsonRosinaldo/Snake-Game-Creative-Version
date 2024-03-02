from turtle import Turtle
from random import choice


UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

SPEED = 11


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.used_colors = []
        self.colors = ["pink", "purple", "green", "blue", "white", "grey", "brown", "yellow", "orange", "violet",
                       "navy blue", "red", "light green", "burgundy"]
        self.color_count = 0
        self.add_segment(choice(self.colors))
        self.head = self.segments[0]

    def add_segment(self, color):
        self.hideturtle()
        new_segment = Turtle("circle")
        new_segment.color("white", color)
        new_segment.pu()
        new_segment.speed("fastest")
        self.segments.append(new_segment)

    def move(self):
        # self.placement()
        self.head.forward(SPEED)

    def lefty(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def righty(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def upy(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def downy(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # def placement(self):  # Now when the snake turns all the body turns having the head as an axis of rotation
    #     for seg in self.segments[1:]:
    #         x = self.segments.index(seg)
    #         seg.setheading(self.segments[x - 1].heading())
    #     for segment in self.segments[:0:-1]:
    #         n = self.segments.index(segment)
    #         minus_n = (len(self.segments)) - n  # Here I deleted the "-1" of len((self.segments) "-1" ) - n. Because
    #         # I want the next item of the list
    #         if self.segments[-1].heading() == UP:
    #             segment.goto((self.segments[::-1][minus_n].xcor()), (self.segments[::-1][minus_n].ycor() - 10))
    #         elif self.segments[-1].heading() == DOWN:
    #             segment.goto((self.segments[::-1][minus_n].xcor()), (self.segments[::-1][minus_n].ycor() + 10))
    #         elif self.segments[-1].heading() == RIGHT:
    #             segment.goto((self.segments[::-1][minus_n].xcor() - 10), (self.segments[::-1][minus_n].ycor()))
    #         elif self.segments[-1].heading() == LEFT:
    #             segment.goto((self.segments[::-1][minus_n].xcor() + 10), (self.segments[::-1][minus_n].ycor()))

    def change_color(self):
        """Depending on the level this assigns a color to a segment of the snake, by level there is only one color
         except the first segment. Returns the new color"""
        if self.color_count == 0:
            new_color = "white"
            self.used_colors.append(new_color)
        elif self.color_count % 10 == 0:
            new_color = choice(self.colors)
            attempt = 0
            go_on = True
            while new_color in self.used_colors and go_on:
                new_color = choice(self.colors)
                attempt += 1
                if attempt > 20:
                    go_on = False
                    print(f"After {attempt} attempts, there is no more colors available")
                    self.color_count = 0
                    self.used_colors = []
                    new_color = "black"
            self.used_colors.append(new_color)
        else:
            new_color = self.used_colors[-1]
        self.color_count += 1
        return new_color

    def restart(self):
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments = []
        self.add_segment(choice(self.colors))
        self.head = self.segments[0]
        self.color_count = 0
        self.used_colors = []

