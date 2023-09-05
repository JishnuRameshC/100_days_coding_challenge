from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    letters_lowercase = [ chr(letter) for letter in range(ord("a"),ord("z"))]
    letters_uppercase = [ chr(letter) for letter in range(ord("A"),ord("Z"))]
    letters = letters_lowercase + letters_uppercase
    numbers = [str(num) for num in range(10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    username = username_entery.get()
    website = website_entry.get()
    password = password_entry.get()
    if len(username) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Oops", message="dont let it empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"your username/email : {username}\n password : {password} \n is it ok to save ?")
        if is_ok:
            with open('data.txt', "a") as file:
                file.write(f"{website} | {username} | {password}  \n")
                password_entry.delete(0,END)
                website_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("password manager")
window.config(padx=50, pady= 50)
logo = PhotoImage(file="logo.png")
canva = Canvas(width=200, height=200)
canva.create_image(100,100,image= logo)
canva.grid(row=0, column=1)

# Label
website_label = Label(text="website")
website_label.grid(row=1,column=0)
username_label = Label(text="email/username")
username_label.grid(row=2,column=0)
password_label = Label(text="Password")
password_label.grid(row=3,column=0)

# Entry
website_entry = Entry(width=60)
website_entry.focus()
website_entry.grid(row=1,column=1, columnspan=3)
username_entery = Entry(width=60)
username_entery.insert(0,"jishnuramesc@gmail.com")
username_entery.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=40)
password_entry.grid(row= 3, column=1)

# Button
generate_password_button = Button(text="generate password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="add",width=50,command=save)
add_button.grid(row=4, column=1,columnspan=2)

window.mainloop()