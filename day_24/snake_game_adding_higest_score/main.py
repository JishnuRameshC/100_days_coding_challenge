from scorebord import Scorebord
from turtle import Screen
import time
from snake import Snake
from food import Food

scorebord = Scorebord()
food = Food()
snake = Snake()
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("snake game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scorebord.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -300:
        scorebord.resets()
        snake.resets()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scorebord.resets()
            snake.resets()

screen.exitonclick()
