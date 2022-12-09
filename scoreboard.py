from turtle import Turtle
import random as rd

FONT = ("Courier", 20, "normal")
GAME_OVER = ["SE FUDEU", "NOSSA VOCÊ É BURRO", "GAME OVER", "NÃO DESISTA", "FRACASSOU"]

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(-50, 0)
        self.write(f"{rd.choice(GAME_OVER)}", align="left", font=FONT)

    pass
