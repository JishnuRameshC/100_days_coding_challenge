import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)
phonetic_dict = {row['letter']:row['code'] for (index,row) in nato_data.iterrows()}
# print(phonetic_dict)
word = input("enter word: ").upper()
nato_output = [phonetic_dict[name] for name in word]
print(nato_output)