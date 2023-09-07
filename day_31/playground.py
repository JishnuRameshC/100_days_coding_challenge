import pandas
import random
data = pandas.read_csv("data/french_words.csv")
to_leran = data.to_dict(orient="records")
print(random.choice(to_leran))
