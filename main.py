from turtle import Turtle, Screen
import time

from snake import Snake

s = Screen()

s.setup(600,600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()

game_over = False
while not game_over:
    s.update()
    time.sleep(0.5)

    snake.snake_move()

s.exitonclick()

