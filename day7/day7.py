# hangman project
from hangman_art import stages,logo
from hangman_words import word_list
import random
dispay = []
chosen_world = random.choice(word_list)
print(chosen_world)
end_of_game = False
life = 5
print(logo)


for i in chosen_world:
    dispay.append('_')

print(dispay)

while not end_of_game:
    guess = input("enter your gess").lower()
    for i in range(len(chosen_world)):
        if chosen_world[i] == guess:
            dispay[i] = chosen_world [i]

    print(dispay)

    if guess not in chosen_world:
        print(f'you choss {guess}  Wrong  ')
        life -= 1
        print(f"your life {life} remaing")
        print(stages[life])
        if life == 0:
            end_of_game = True
            print("you loss")

        
    

    if "_" not in dispay:
        end_of_game = True
        print("you win")