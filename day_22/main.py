from turtle import Turtle,Screen
from scorebord import Scorebord
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
scorebord = Scorebord()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

ball = Ball()

l_paddle = Paddle((-375,0))
r_paddle = Paddle((375,0))

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collition ball hit wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collition ball hit paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        

    # detect right Paddle misses
    if ball.xcor() > 360:
        scorebord.l_point()
        ball.reset_position()
        print("Left Score:", scorebord.l_score)


    # detect left Paddle misses
    if ball.xcor() < -360:
        scorebord.r_point()
        ball.reset_position()
        print("Right Score:", scorebord.r_score)



screen.exitonclick()
