from turtle import Screen
import time as t
from snake import Snake
from food import Food
from score import ScoreBoard

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


def clear_count():
    screen.update()
    t.sleep(0.8)
    score.clear()


def count_down():
    score.regressive_3()
    clear_count()
    score.regressive_2()
    clear_count()
    score.regressive_1()
    clear_count()
    score.go()
    clear_count()
    score.create_score()


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game Jonilson's Version")
screen.tracer(0)
screen.listen()

snake = Snake()

food = Food()

score = ScoreBoard()

screen.onkey(key="Up", fun=snake.upy)
screen.onkey(key="Down", fun=snake.downy)
screen.onkey(key="Left", fun=snake.lefty)
screen.onkey(key="Right", fun=snake.righty)
screen.onkey(key="w", fun=snake.upy)
screen.onkey(key="s", fun=snake.downy)
screen.onkey(key="a", fun=snake.lefty)
screen.onkey(key="d", fun=snake.righty)

print("segments are: ", len(snake.segments))  # Delete

sleep = 0.07
play_on = True
while play_on:
    t.sleep(sleep)
    for segment in snake.segments[:0:-1]:
        n = snake.segments.index(segment)
        segment.goto(snake.segments[n - 1].pos())
    snake.move()
    if score.score > 15:
        food.move()
    screen.update()

    screen.tracer(0)
    if snake.head.distance(food) < 16:
        if not (-330 < food.xcor() < 330) or not (330 > food.ycor() > -330) and score.score > 15:
            score.add_half()
        else:
            score.add_1()
        food.food_eaten()
        snake.add_segment(snake.change_color())

        # Increases the speed after leveling up
        if score.score > 1 and (score.score % 10 == 0 or score.score % 10 == 0.5) and sleep > 0.01:
            sleep -= 0.01
            score.level_up()  # Each 5 + 0.5 levels up the game
            screen.update()   # Super important to update the screen so that I can see the differences displayed.
            t.sleep(1.5)
            score.clear()
            if score.level == 1:
                score.lets_see(snake.head.ycor())
                screen.update()
                t.sleep(4)
                score.clear()
            count_down()  # This is a function that counts regressively until the game is back on
        if score.score == 16:
            score.catch_the_food()
            screen.update()
            t.sleep(4)
            score.clear()
            score.create_score()
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 340 or snake.head.ycor() < -330:
        score.game_over("You hit the wall")
        screen.update()
        snake.restart()
        score.restart()
        score.clear()
        t.sleep(4)
        count_down()
        sleep = 0.07

    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            score.game_over("You hit the tail")
            screen.update()
            score.clear()
            t.sleep(4)
            snake.restart()
            score.restart()
            count_down()
            sleep = 0.07

# Had a bug when screen was sleeping and snake stopped upon segment (perhaps have to fix the order the code is written)

screen.exitonclick()
