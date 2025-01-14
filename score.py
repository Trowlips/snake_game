from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.goto((-20, 280))
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", True, align="left", font=("Arial", 12, "normal"))

    def add_score(self):
        self.score += 1
        self.undo()
        self.write_score()

    def game_over(self):
        self.home()
        self.clear()
        self.write(f"Game Over! your final score is {self.score}", True, align="center", font=("Arial", 15, "normal"))