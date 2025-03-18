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
WORK_MIN = 25
SHORT_BREAK_MIN = 1
# Long Break each 2 hours 
LONG_BREAK_MIN = 10
# 8 sections for 2 hours, 16 for 4 hours 
TOTAL_SECTIONS = 16
LONG_BREAK_SECTION = 8

work_sec = int(WORK_MIN * 60)
short_break_sec = int(SHORT_BREAK_MIN * 60)
long_break_sec = int(LONG_BREAK_MIN * 60)
reps = 0
is_stop_timer = False
is_break = True
checkmark_text = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)

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

def skip_break():
    global reps
    reps += 1
    canvas.itemconfig(timer_text, text="00:00")
    working_time()
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def working_time():
    winsound.Beep(1000, 1000)
    
    global is_break
    is_break = False
    focus_window("off")
    skip_break_button.config(state="disabled")
    countdown_working(work_sec)
    title_label.config(text="Working Time", fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
    notification.notify(
        title='Pomodoro',
        message='Start working now',
        app_icon=os.path.join(os.path.dirname(__file__), 'tomato.ico'),
        timeout=10,
    )

def break_time(break_time, break_title):
    winsound.Beep(1111, 1111)
    
    global is_break
    is_break = True 
    focus_window("on")
    countdown_break(break_time)
    title_label.config(text=break_title, fg=RED, font=(FONT_NAME, 30), bg=YELLOW)
    global checkmark_text
    checkmark_text += CHECK_MARK
    checkmark_label.config(text=checkmark_text, fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW)
    skip_break_button.config(state="active") 
    
def start_timer():
    global reps
    reps += 1
    global is_stop_timer
    is_stop_timer = False
    
    if reps % LONG_BREAK_SECTION == 0:
        break_time(long_break_sec, "Long Break")
    elif reps % 2 == 1:
        working_time()
    else:
        break_time(short_break_sec, "Short Break")
    start_button.config(state="disabled")   

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- 
def countdown_break(count):
    if is_stop_timer :
        return
    if not is_break :
        return 
    canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")
    if count > 0:
        window.after(1000, countdown_break, count - 1)
    elif reps < TOTAL_SECTIONS:
        start_timer()
    else:
        winsound.Beep(1414, 1414)
        title_label.config(text="Well Done! You did it!", fg=RED, font=(FONT_NAME, 20), bg=YELLOW)
        skip_break_button.config(state="disabled")
    
def countdown_working(count):
    if is_stop_timer :
        return
    # print(f"countdown {count}")
    canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")
    if count > 0:
        window.after(1000, countdown_working, count - 1)
    elif reps < TOTAL_SECTIONS:
        start_timer()
    else:
        winsound.Beep(1414, 1414)
        title_label.config(text="Well Done! You did it!", fg=RED, font=(FONT_NAME, 20), bg=YELLOW)
        skip_break_button.config(state="disabled")

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

skip_break_button = Button(text="Skip Break Time", command=skip_break, bg=YELLOW, fg=RED, font=(FONT_NAME, 10))
skip_break_button.grid(row=4, column=1)
skip_break_button.config(state="disabled")

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, fg=RED, font=(FONT_NAME, 15))
reset_button.grid(row=2, column=2)

checkmark_label = Label(text="", fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()