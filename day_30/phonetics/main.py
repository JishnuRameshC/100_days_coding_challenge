import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)
phonetic_dict = {row['letter']:row['code'] for (index,row) in nato_data.iterrows()}
# print(phonetic_dict)

def generate_phonetics():
    word = input("enter word: ").upper()
    try:    
        nato_output = [phonetic_dict[name] for name in word]
    except KeyError:
        print("sorry only alphabet plss")
        generate_phonetics()
    else:
        print(nato_output)

generate_phonetics()