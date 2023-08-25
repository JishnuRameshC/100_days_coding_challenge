from turtle import Turtle 
from random import choice
colors = ['brown', 'red','medium slate blue', 'purple']
turtle = Turtle()
for i in range(3,1000):
    turtle.color(choice(colors))
    for j in range(i):
        degree = 360 / i
        turtle.forward(100)
        turtle.right(degree)


