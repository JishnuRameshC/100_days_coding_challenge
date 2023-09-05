import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def rest_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    title_label.config(text="Timer")
    check_label.config(text="")
    canva.itemconfig(timer_text,text = "00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_min = WORK_MIN
    short_break = SHORT_BREAK_MIN
    long_break = LONG_BREAK_MIN
    if reps % 8 == 0:
        title_label.config(text="long break")
        count_down(long_break * 60)
    elif reps % 2 == 0:
        title_label.config(text="stort break")        
        count_down(short_break * 60)
    else:
        title_label.config(text="work")
        count_down(work_min * 60)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60 
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canva.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sections = math.floor(reps/2)
        for i in range(work_sections):
            marks += "✅"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodora app")
window.config(padx=100, pady=50, bg=YELLOW)

canva = Canvas(width=200, height=224, bg= YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canva.create_image(102,102,image=tomato_img)
timer_text = canva.create_text(100,120, text="00:00", font=(FONT_NAME,40,"bold"), fill="white")
canva.grid(column=2,row=2)

title_label = Label(text="Timer",bg=YELLOW, fg=GREEN,font=(FONT_NAME,50,"bold"))
title_label.grid(column=2, row=1)

start_button = Button(text="start", command=start_timer)
start_button.grid(column=1,row=3)

reset_button = Button(text="reset",command= rest_timer)
reset_button.grid(column=3,row=3)

check_label = Label(bg=YELLOW, fg=GREEN,font=(FONT_NAME,20,"bold"))
check_label.grid(column=2, row=4)

window.mainloop()
