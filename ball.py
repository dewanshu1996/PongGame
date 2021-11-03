from turtle import Turtle

ball_moment = 15

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.initial_direction_y = "UP"
        self.initial_direction_x = "LEFT"

    def move_ball(self):
        self.check_boundry_collision()
        if self.initial_direction_y == "UP":
            new_y_pos = self.ycor() + ball_moment
        else:
            new_y_pos = self.ycor() - ball_moment

        if self.initial_direction_x == "RIGHT":
            new_x_pos = self.xcor() + ball_moment
        else:
            new_x_pos = self.xcor() - ball_moment

        self.goto(x=new_x_pos, y=new_y_pos)

    def check_boundry_collision(self):
        if self.initial_direction_y == "UP":
            if self.ycor() > 280:
                self.initial_direction_y = "DOWN"
        else:
            if self.ycor() < -280:
                self.initial_direction_y = "UP"

    def reverse_x_dir(self):
        if self.initial_direction_x == "LEFT":
            self.initial_direction_x = "RIGHT"
        else:
            self.initial_direction_x = "LEFT"

    def reset_position(self):
        self.goto(x=0, y=0)
        self.reverse_x_dir()

