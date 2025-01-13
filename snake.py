from turtle import Turtle


class Snake:
    def __init__(self):

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
        self.snake_body[0].forward(20)

    # def turn_right(self):
    #     self.snake_body[0].right(90)
    #
    # def turn_left(self):
    #     self.snake_body[0].right(90)