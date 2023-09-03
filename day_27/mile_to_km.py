from tkinter import *

def mile_to_km():
    mile = float(input.get())
    km = mile * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
FONT = ("arial",20)
window.title("mile to km")
window.config(padx=20,pady=20)

miles_label =Label(text="miles", font=FONT)
miles_label.grid(column=3, row=0)

equal_to_label = Label(text="equal to", font=FONT)
equal_to_label.grid(column=1, row=1)

km_result_label = Label(text="0", font=FONT)
km_result_label.grid(column=2, row=1)

km_label = Label(text="km", font=FONT)
km_label.grid(column=3, row=1)

button = Button(text="clike me", font=FONT,command=mile_to_km)
button.grid(column=2, row=2)

input = Entry(width=7, font=FONT)
input.grid(column=2, row=0)

window.mainloop()