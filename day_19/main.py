from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pencolor("white")
screen.bgcolor("black")
tim.color("white")

def move_forward():
    tim.forward(50)


def move_backward():
    tim.back(50)


def turing_right():
    new_heading =tim.heading() + 20
    tim.setheading(new_heading)


def turing_left():
    new_heading =tim.heading() - 20
    tim.setheading(new_heading)


def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(turing_right, "d")
screen.onkey(turing_left,"a")
screen.onkey(clear_screen,"space")
screen.exitonclick()