from tkinter import *


window = Tk()
window.title("this is my title")
window.minsize(width=500,height=300)

# Label

my_label = Label(text="this is my label", font=("arial",20, "bold"))
my_label.grid(column=0, row=0)
# my_label["text"] = "new text"
my_label.config(text="new text")
# button


def butten_clicked():
    new_text = entery.get()
    my_label.config(text= new_text)


entery = Entry(width=20)
entery.grid(column=3,row=2)
print(entery.get())

my_button = Button(text="click me", command=butten_clicked)
my_button.grid(column=1,row=1)

new_button = Button(text="button 2", command=butten_clicked)
new_button.grid(column=2,row=0)











window.mainloop()