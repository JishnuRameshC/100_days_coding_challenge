import turtle as t
import random
t.colormode(255)
tim = t.Turtle()

diretions = [0, 90, 180,270]
# color_list = ["red", "green", "blue", "orange", "purple", "pink", "cyan", "brown", "yellow", "gray"]
tim.speed(50)
tim.pensize(15)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


for _ in range(2000):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(diretions))
