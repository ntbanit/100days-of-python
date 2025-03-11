from tkinter import *
from plyer import notification
import winsound
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK="✔"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1

work_sec = int(WORK_MIN * 60)
short_break_sec = int(SHORT_BREAK_MIN * 60)
long_break_sec = int(LONG_BREAK_MIN * 60)
reps = 0
is_stop_timer = False
checkmark_text = ""
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    global is_stop_timer
    is_stop_timer = True
    start_button.config(state="active")
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Pomodoro Timer", fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
    global checkmark_text
    checkmark_text = ""
    checkmark_label.config(text=checkmark_text, fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    global is_stop_timer
    is_stop_timer = False
    global checkmark_text
    winsound.Beep(1000, 1000)
    if reps == 8:
        countdown(long_break_sec)
        title_label.config(text="Long Break", fg=RED, font=(FONT_NAME, 30), bg=YELLOW)
        checkmark_text += CHECK_MARK
        checkmark_label.config(text=checkmark_text, fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW)
        
    elif reps % 2 == 1:
        countdown(work_sec)
        title_label.config(text="Working Time", fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
        notification.notify(
            title='Pomodoro',
            message='Start working now',
            app_icon=os.path.join(os.path.dirname(__file__), 'tomato.ico'),
            timeout=10,
        )
    else:
        # Display checkmark 
        checkmark_text += CHECK_MARK
        checkmark_label.config(text=checkmark_text, fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW)
        countdown(short_break_sec)
        title_label.config(text="Short Break", fg=PINK, font=(FONT_NAME, 30), bg=YELLOW)
        
    start_button.config(state="disabled")
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- 
def countdown(count):
    if is_stop_timer :
        return
    # print(f"countdown {count}")
    canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    elif reps < 8:
        start_timer()
    else:
        title_label.config(text="Well Done! You did it!", fg=RED, font=(FONT_NAME, 20), bg=YELLOW)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer") 
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas( width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30), fill=YELLOW)
canvas.grid(row=1, column=1)


title_label = Label(text="Pomodoro Timer", fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, bg=YELLOW, fg=RED, font=(FONT_NAME, 15))
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, fg=RED, font=(FONT_NAME, 15))
reset_button.grid(row=2, column=2)

checkmark_label = Label(text="", fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()