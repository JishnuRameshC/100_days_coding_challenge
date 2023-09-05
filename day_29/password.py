
from random import randint, choice, shuffle


letters_lowercase = [ chr(letter) for letter in range(ord("a"),ord("z"))]
letters_uppercase = [ chr(letter) for letter in range(ord("A"),ord("Z"))]
letters = letters_lowercase + letters_uppercase
numbers = [str(num) for num in range(10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_letters = [choice(letters) for char in range(randint(8, 10))]
password_symbols = [choice(symbols) for char in range(randint(2, 4))]
password_numbers = [choice(numbers) for char in range(randint(2, 4))]

password_list = password_letters + password_numbers + password_symbols
shuffle(password_list)

password = "".join(password_list)
print(f"Your password is: {password}")