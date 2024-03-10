from turtle import Turtle, Screen
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1


class Padel(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=6)
        self.goto(self.x, self.y)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())


class Box(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=5)
        self.goto(self.x, self.y)


time_delay = 0.1
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Brakeout")
screen.tracer(0)
ball = Ball()
screen.listen()
padel = Padel(0, -350)
screen.onkey(padel.go_right, "d")
screen.onkey(padel.go_left, "a")
game_is_on = True

boxes_list = []
for y in [(370, "red"), (320, "orange"), (270, "yellow")]:
    for x in [-420, -320, -220, -120, -20, 80, 180, 280, 380]:
        boxes_list.append(Box(x, y[0], y[1]))


def check_if_box_hit():
    global time_delay
    for object in boxes_list:
        if ball.distance(object) < 40:
            object.hideturtle()
            boxes_list.remove(object)
            ball.bounce_y()
            time_delay -= 0.01


while game_is_on:
    time.sleep(time_delay)
    screen.update()
    ball.move()
    if ball.ycor() < -390:  # if hits ground it resets and goes up
        ball.goto(0, 0)
        ball.bounce_y()
    if ball.ycor() > 390:  # if it hits selaing it bounces
        ball.bounce_y()
    if ball.distance(padel) < 35 and ball.ycor() > -360:  # if ball hits padel then it bounces
        ball.bounce_y()
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()
    if ball.ycor() > 250:
        check_if_box_hit()
    if not boxes_list:
        game_is_on = False
