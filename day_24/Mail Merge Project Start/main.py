#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


name_list = []


with open('Input/Letters/starting_letter.txt', 'r') as letter_file:
    starting_letter = letter_file.read()


with open('Input/Names/invited_names.txt','r') as names_file:
    for line in names_file:
        name_list.append(line.strip())


for name in name_list:
    new_letter = starting_letter.replace('[name]', name)
    with open(f'Output\ReadyToSend\sending_to_{name}', 'w') as file:
        file.write(new_letter)