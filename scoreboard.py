from turtle import Turtle
FONT = ("courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 260)
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def level_update(self):
        self.level += 1
        self.scoreboard_update()

    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.hideturtle()
        self.write("Game Over", align="center", font=FONT)
