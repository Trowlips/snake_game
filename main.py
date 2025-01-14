from turtle import Screen
import time
from food import Food
from snake import Snake
from score import Score

s = Screen()

s.setup(600,600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

s.listen()
s.onkey(snake.move_up, "Up")
s.onkey(snake.move_down, "Down")
s.onkey(snake.move_right, "Right")
s.onkey(snake.move_left, "Left")

game_over = False

def game_over_func():
    global game_over
    snake.snake_head.color("red")
    s.update()
    game_over = True
    score.game_over()

while not game_over:
    s.update()
    time.sleep(0.1)

    snake.snake_move()
    snake_head_xcor = snake.snake_head.xcor()
    snake_head_ycor = snake.snake_head.ycor()

    if snake.snake_head.distance(food) < 15:
        print("EAT")
        score.add_score()
        snake.add_body()
        food.spawn_random()

    if snake_head_xcor > 290 or snake_head_xcor < -290 or snake_head_ycor > 290 or snake_head_ycor < -290:
        game_over_func()

    for body in snake.snake_body[3:]:
        if snake.snake_head.distance(body) < 10:
            body.color('red')
            game_over_func()


s.exitonclick()

