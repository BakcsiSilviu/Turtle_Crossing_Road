from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.spawn_turtle()

    def spawn_turtle(self):
        self.player = Turtle("turtle")
        self.player.color("white")
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)

    def move_up(self):
        self.player.goto(self.player.xcor(), self.player.ycor() + MOVE_DISTANCE)
    
    def move_right(self):
        if self.player.xcor() > 270:
            pass
        else:
            self.player.goto(self.player.xcor() + MOVE_DISTANCE, self.player.ycor())

    def move_left(self):
        if self.player.xcor() < -270:
            pass
        else:
            self.player.goto(self.player.xcor() - MOVE_DISTANCE, self.player.ycor())

    def finish_level(self):
        if self.player.ycor() > 280:
            self.player.reset()
            return True
        else:
            return False