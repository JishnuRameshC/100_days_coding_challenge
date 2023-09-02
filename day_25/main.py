# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
    

import csv

# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

# print(temperature)



# import pandas

# data = pandas.read_csv("weather-data.csv")
# print(data["temp"])

# print(data.to_dict())
# temperature = data["temp"].to_list()
# print(sum(temperature)/len(temperature))
# print(data["temp"].mean())
# print(data["temp"].max())


# # get data coloum
# print(data["condition"])
# print(data.condition)

# # get data in row
# print(data[data.day == "Monday"])
# print(max(data["temp"] ))
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp_C = int(monday.temp)
# monday_temp_F = (monday_temp_C *9/5) +32
# print(monday_temp_F)

# # creating dataframe from scrach

# data_dict = {
#     "student": ["anna","onepunchman", "jorge", "godzila", "thanoz"],
#     "score" : [49, 999999, 29, 394, 350]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv ")


import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"]== "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"]== "Black"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"]== "Cinnamon"])
print(black_squirrel_count,cinnamon_squirrel_count, gray_squirrel_count)


data_dict = {
    "Primary Fur Color" : ["Gray", "Black", "cinnamon"],
    "count" : [gray_squirrel_count, black_squirrel_count, cinnamon_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel count.csv")