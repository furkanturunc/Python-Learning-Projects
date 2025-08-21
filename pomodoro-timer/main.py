from tkinter import *
import math
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
def reset_timer():
    global reps, timer
    reps = 0
    window.after_cancel(timer)
    label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label2.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 2 == 1:
        label.config(text="Work", fg=GREEN)
        count_down(work_seconds)
    elif reps % 2 == 0 and reps % 8 != 0:
        label.config(text="Break", fg=PINK)
        count_down(short_break_seconds)
    else:
        label.config(text="Break", fg=RED)
        count_down(long_break_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = int(count / 60)
    seconds = count % 60

    # Dynamic Typing in Python (variable type changes from int to string)
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down,count - 1)
    else:
        if reps % 2 == 1:
            text = "✔" * math.ceil(reps / 2)
            label2.config(text=text)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image = PhotoImage(file="images/tomato.png")
canvas.create_image(100,112,image=image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# Timer Label
label = Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

# Checkmark Text
label2 = Label(fg=GREEN,bg=YELLOW)
label2.grid(column=1,row=3)

# Start Button
button = Button(text="Start",bg=YELLOW,highlightbackground=YELLOW, command=start_timer)
button.grid(column=0,row=2)

# Reset Button
button = Button(text="Reset",bg=YELLOW,highlightbackground=YELLOW, command=reset_timer)
button.grid(column=2,row=2)

window.mainloop()