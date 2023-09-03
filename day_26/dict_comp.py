# # dictory comprehensions 
# import random
# names = ["jrc", "cj", "nebula", "vesana", "jhonson" ]

# scores = {name:random.randint(1,100) for name in names}

# print(scores)
# passed = {name:score for (name,score) in scores.items() if score >= 60 }
# print(passed)

# sendence = "one shot one kill"

# new_dict = {line:len(line) for line in sendence.split()}
# print(new_dict)

# weather_c = {
#     "Monday":25,
#     "thusday":12,
#     "wednesday":14,
#     "thursday":22,
#     "friday":13,
#     "sunday":15
# }
# weather_f ={ day:(temp_c*9/5) +32  for (day,temp_c) in weather_c.items()}
# print(weather_c)
# print(weather_f)

students = {
    "name": ["gamora", "titan", "panda", "sun", "sabir"],
    "score": [34, 36, 47, 37, 57]
}

# # looping throug dictionary
# for (key,value) in students.items():
#     print(key)
#     print(value)

import pandas

students_dataframe = pandas.DataFrame(students)
print(students_dataframe)

# # looping through dataframe
# for (key,value) in data.items():
#     print(key)
#     print(value)

for (index,row) in students_dataframe.iterrows():
    if row["name"] == "gamora":
        print(row)