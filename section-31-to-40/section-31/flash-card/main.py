from tkinter import *
from my_dictionary import WordLearningDictionary
# ---------------------------- GLOBAL VARIABLES ----------------------  #
"""
Every time you press the ❌ or ✅ buttons, it should generate a new random word to display. 
"""
learning_dict = WordLearningDictionary()
flip_timer = False
current_word = None
count = 0

# ---------------------------- EVENT ---------------------------------- #
def on_closing():
    # Save the remaining words to learn
    learning_dict.save_progress()
    window.destroy()
def next_word_event():
    global current_word, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)

    current_word = learning_dict.generate_new_word()
    card_front_canvas.delete("all")
    card_front_canvas.create_image(400, 263, image=card_front_image)
    card_front_canvas.create_text(400, 150, text="English", font=("Ariel", 40))
    card_front_canvas.create_text(400, 263, text=current_word["English"], font=("Ariel", 60))
    # fliping card after 5 seconds 
    flip_timer = window.after(5000, flip_word_event)

def flip_word_event():
    card_front_canvas.delete("all")
    card_front_canvas.create_image(400, 263, image=card_back_image)
    card_front_canvas.create_text(400, 150, text="IPA Pronunciation", fill='#FFFFFF', font=("Ariel", 40))
    card_front_canvas.create_text(400, 263, text=current_word["IPA"], fill='#FFFFFF', font=("Ariel", 60))

def tick_word_event():
    if current_word != '':
        learning_dict.tick_word_event()
    next_word_event()
    global count, count_label
    count += 1
    count_label.config(text="Count of words learned today: " + str(count))
    
def cross_word_event():
    next_word_event()

def tick_word_event_bind(event):
    tick_word_event()
def cross_word_event_bind(event):
    cross_word_event()

# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards") 
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=tick_word_event,  highlightthickness=0)
# Bind the right keyboard to tick word event

right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,  command=cross_word_event, highlightthickness=0)
wrong_button.grid(row=1, column=0)

card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")

card_front_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_canvas.grid(row=0, column=0, columnspan=2)

count_label = Label(text="Count words learn today: " + str(count), fg="#212121", bg=BACKGROUND_COLOR, font=("Ariel", 40))
count_label.grid(row=2, column=0, columnspan=2)
tick_word_event()

window.bind("<Escape>", on_closing)  # pressing escape key will close the window
# pressing space
window.bind("<space>", tick_word_event_bind)
# pressing x
window.bind("<x>", cross_word_event_bind)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
