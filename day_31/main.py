from tkinter import *
import pandas,random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orginal_data = pandas.read_csv("data/french_words.csv")
    to_leran = orginal_data.to_dict(orient="records")
else:
    to_leran = data.to_dict(orient="records")



def next_card():
    global current_card,flip
    window.after_cancel(flip)
    current_card = random.choice(to_leran)
    french_word = current_card["French"]
    canva.itemconfig(canva_text, text=french_word,fill="black")
    canva.itemconfig(canva_title,text = "French",fill="black")
    canva.itemconfig(canva_bg,image= card_front_img)
    window.after(3000,func=flipcard)


def flipcard():
    english_word = current_card["English"]
    canva.itemconfig(canva_title,text = "English",fill= "white")
    canva.itemconfig(canva_text,text = english_word,fill = "white")
    canva.itemconfig(canva_bg,image= card_back_img)


def is_known():
    global to_leran
    data = pandas.DataFrame(to_leran)
    data.to_csv("data/words_to_learn.csv",index=False)
    to_leran.remove(current_card)
    print(len(to_leran))
    next_card()
    

window = Tk()
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip = window.after(3000,func=flipcard)
canva = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
# img files
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
card_front_img = PhotoImage(file="images/card_front.png")
wrong_img = PhotoImage(file="images/wrong.png")

canva_bg = canva.create_image(400,264,image = card_front_img)
canva_title = canva.create_text(400, 150,text="ramdom",font=("arial", 53))
canva_text = canva.create_text(400, 300,text="ramdom",font=("arial", 53))
canva.grid(row=0, column=0, columnspan=2)
# Button
unknown_button = Button(image=wrong_img, command=next_card)
unknown_button.grid(row=1,column=0)
check_button = Button(image=right_img,command=is_known)
check_button.grid(row=1, column=1)

next_card() 
window.mainloop()
