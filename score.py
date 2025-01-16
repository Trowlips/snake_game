from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        # self.high_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        # self.speed("fastest")
        self.goto((0, 280))
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, align="center", font=("Arial", 12, "normal"))

    def add_score(self):
        self.score += 1
        # self.undo()
        self.write_score()

    # def game_over(self):
    #     self.home()
    #     self.clear()
    #     self.write(f"Game Over! your final score is {self.score}", True, align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()

        with open("data.txt", "w") as file:
            file.write(str(self.high_score))
