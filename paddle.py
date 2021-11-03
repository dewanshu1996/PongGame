from turtle import Turtle

UP = 90
DOWN = 270
INCREMENT = 10

paddle_moment = 25


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1, 1)

        if pos == "LEFT":
            self.goto(x=-370, y=0)
        else:
            self.goto(x=370, y=0)

    def up(self):
        if self.ycor() < 280:
            new_pos_x = self.xcor()
            new_pos_y = self.ycor() + paddle_moment
            self.goto(x=new_pos_x, y=new_pos_y)

    def down(self):
        if self.ycor() > -280:
            new_pos_x = self.xcor()
            new_pos_y = self.ycor() - paddle_moment
            self.goto(x=new_pos_x, y=new_pos_y)
