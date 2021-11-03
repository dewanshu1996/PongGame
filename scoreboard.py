from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_of_left = 0
        self.score_of_right = 0
        self.rwrite_message()


    def rwrite_message(self):
        self.clear()
        self.goto(x=-40, y=230)
        self.write(self.score_of_left , align="center" , font=("Courier" , 50  , "normal"))
        self.goto(x=40, y=230)
        self.write(self.score_of_right , align="center" , font=("Courier" , 50  , "normal"))


    def set_score_of_left_player(self):
        self.score_of_left += 1
        self.rwrite_message()


    def set_score_of_right_player(self):
        self.score_of_right += 1
        self.rwrite_message()

    def print_game_over_message(self):
        if self.score_of_left == 10:
            message = "Left player won"
        else:
            message = "Right player is won"

        self.goto(x=-0, y=0)
        self.write("Game Over", align="center", font=("Courier", 100, "normal"))
        self.goto(x=-0, y=150)
        self.write(message, align="center", font=("Courier", 50, "normal"))