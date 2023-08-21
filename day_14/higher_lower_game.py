import random,os
from game_data import data
from art import vs,logo
def get_random():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    follower = account["follower_count"]
    return f"{name}, a {description}, from {country} (only for testing: {follower})"


game_over = False
a = get_random()
b = get_random()
answer = ''

while not game_over :
    if answer == '1' :
        b = get_random()
    elif answer == "2" :
        a = b
        b= get_random()

    if a == b:
        b = get_random()

    print(logo)
    print('What gets Googled more?')
    print(f"1 {format_data(a)}")
    print(vs)
    print(f"2 {format_data(b)}")
    choice = input(f"1:{a['name']} 0r 2:{b['name']} who gets Googled more?:  ")  

    if a['follower_count'] < b['follower_count']:
        answer = '2'
    elif a['follower_count'] > b['follower_count']:
        answer = "1"

    if choice == '1' and choice == answer:
        print('succes')
        os.system('cls')
    elif choice == '2' and choice == answer:
        print("succes") 
        os.system('cls')
    else:
        print("you loss")
        game_over = True






