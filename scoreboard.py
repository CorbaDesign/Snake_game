from turtle import Turtle

FONT = "Courier", 24, "italic"
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER ", align=ALIGNMENT, font=FONT)

    def add_score(self):
        print("score update")
        self.score = self.score + 1
        self.clear()
        self.update_score()
