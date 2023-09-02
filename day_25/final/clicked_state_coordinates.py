import turtle
import pandas

data = pandas.read_csv("indian_state.csv")
print(data["state"])
states = data["state"]
coordinates = {
    "x_coordinate": [],
    "y_coordinate": [],
    "state_name": []
}


screen = turtle.Screen()
screen.title("india state game")
image = "india.gif"
screen.addshape(image)
new_turtle = turtle.Turtle()
new_turtle.color("red")
new_turtle.dot(20)

def get_mouse_click_coor(x, y):
    print(x, y)

    new_turtle.goto(x, y)
    state_index = turtle.numinput("Click on a state", "Enter the state number:")
    if 0 <= state_index < len(states):
        state_name = states[state_index]
        print(f"Clicked on: {state_name}")
        coordinates["x_coordinate"].append(x)
        coordinates["y_coordinate"].append(y)
        coordinates["state_name"].append(state_name)


screen.onscreenclick(get_mouse_click_coor)
turtle.shape(image)


screen.mainloop()
result_df = pandas.DataFrame(coordinates)
result_df.to_csv("clicked_state_coordinates.csv", index=False)