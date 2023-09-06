from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
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
    new_data = {
        website:{
            'username':username,
            'password':password
        }
    }
    if len(username) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Oops", message="dont let it empty")
    else:
        try:
            with open('data.json', "r") as data_file:
                # read old data
                data =json.load(data_file)
                
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # savind updated data
                json.dump(data,data_file, indent=4)
        finally:
            password_entry.delete(0,END)
            website_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError as fnf:
        messagebox.showwarning(title=fnf , message=f"{fnf} error detected")
    else:        
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"usernaem : {username}\npassword : {password}")
            print(data[website])
        else:
            messagebox.showinfo(title=website, message=f"  no data exit for the {website}")
   
    

    
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
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1,column=1)
username_entery = Entry(width=60)
username_entery.insert(0,"jishnuramesc@gmail.com")
username_entery.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=40)
password_entry.grid(row= 3, column=1)

# Button
generate_password_button = Button(text="generate password",command=generate_password,width=15)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="add",width=50,command=save)
add_button.grid(row=4, column=1,columnspan=2)
search_button = Button(text="search", command=find_password,width=15)
search_button.grid(row=1,column=2)
window.mainloop()