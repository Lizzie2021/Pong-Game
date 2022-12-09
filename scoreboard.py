from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.middle_line()

    def l_points(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_points(self):
        self.r_score += 1
        self.update_scoreboard()

    def middle_line(self):
        self.goto(0, 300)
        self.setheading(270)
        self.pensize(4)
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
