import random
from art import logo
import os 
# from random import randint
# numbers = randint(1,100)


def guess():
    print("welcome to the Number gussing game ")
    print("i am thinking a number between 1 to 100 ")
    numbers = [i for i in range(1,101)]
    life = 0
    print(logo)
    comp_no = random.choice(numbers)
    end_game = False
    level = input("enter your level  E for easy  H for hard :")
    if level == "H":
        life = 5
    elif level == "E":
        life = 10
    else:
        life = 10
    
    print(comp_no)
    while not end_game:
        user_no = int(input("MAKE A GUESS : "))
        if user_no == comp_no:
            print("U WON 😊")
            end_game = True
        elif user_no > comp_no:
            print("too long")
        elif user_no < comp_no:
            print("too short")
        print(f" you have {life } attempt remaing ")
        if life == 0:
            end_game = True
            print("you loss  🦆")
        
        life -= 1
    if input("do you want to continue new game type Y  :") == 'Y':
        os.system('cls')
        guess() 
guess()   