from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake_speed = MOVE_DISTANCE
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        snake_body = []
        for body in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake_body.append(snake)

            if body > 0:
                prev_body_pos = snake_body[body - 1].xcor()
                snake_body[body].setx(prev_body_pos - 20)

        self.snake_body = snake_body

    def snake_move(self):
        for body in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].setpos((new_x, new_y))
        self.snake_head.forward(self.snake_speed)

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def add_body(self):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        last_body_index = len(self.snake_body) - 1
        last_body_pos = self.snake_body[last_body_index].pos()
        snake.goto(last_body_pos)
        self.snake_body.append(snake)