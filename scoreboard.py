from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.color("White")
        self.scoreboard.penup()
        self.scoreboard.goto(190, 275)
        self.score_track()

    def score_track(self):
        self.level += 1
        self.scoreboard.clear()
        self.scoreboard.write(arg= f"Level:{self.level}", font= FONT)

    def defeat(self):
        self.lose = Turtle()
        self.lose.color("white")
        self.lose.hideturtle()
        self.lose.penup()
        self.lose.goto(-65, 0)
        self.lose.write(arg= f"GAME OVER!", font= FONT)
        
