import turtle
import pandas


data = pandas.read_csv("50_states.csv") 
all_state = data.state.to_list()
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("state game ")
screen.addshape(image)
turtle.shape(image)
guessed_states = []


while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 of guessed",prompt="what's another state name").title()
    print(answer)
    if answer == "Exit":
        missing_states = [state for state in all_state if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")


    if answer in all_state:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data.state == answer]
        t.goto(int(row.x), int(row.y))
        t.write(answer)

