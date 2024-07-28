FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.update()
    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
    def increment_level(self):
        self.level += 1
        self.update()
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!! ", align=ALIGNMENT, font=FONT)
