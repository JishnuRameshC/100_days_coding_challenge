import pandas
from turtle import Turtle, Screen


data = pandas.read_csv("list_of_states_in_india-28j.csv")
states = data["State"]
zone = data["Zone"]
vehicle_code = data["Vehicle code"]

data_dict = {
    "state":states.to_list(),
    "zone" :zone.to_list(),
    "vehicle_code":vehicle_code.to_list()
}
df = pandas.DataFrame(data_dict)
df.to_csv("indian_state.csv")