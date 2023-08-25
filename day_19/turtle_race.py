from turtle import Turtle, Screen
import random
is_game_on = False
screen = Screen()
screen.setup(width=500,height=400)
screen.bgcolor("black")
color_list = ["white","green", "blue", "red", "purple", "yellow","orange"]
position = [120,-120,80,-80,40,-40, 0]
user_bet = screen.textinput(title="make a guess ", prompt="which turtile will win ? enter the color :")
print(user_bet)
turtle_list = []

for i in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=position[i] )
    turtle_list.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 220:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you win!! {winning_color} is the winner")
            else:
                print(f"you loss!! {winning_color} is the winner")
        random_distance = random.randint(1,10)
        turtle.forward(random_distance)
screen.exitonclick()