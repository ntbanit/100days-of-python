from tkinter import *
# ---------------------------- GLOBAL VARIABLES ----------------------  #
"""
Read the data from the english_ipa_words.csv file in the data folder.
Pick a random word/IPA pronunciation and put the word into the flashcard.
Every time you press the ❌ or ✅ buttons, it should generate a new random word to display. 
"""
import pandas
import random
word_df = None
count = 0
try :
    # not first time the program runs, read the saved file
    word_df = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    # first time the program runs, read the original file
    word_df = pandas.read_csv("data/english_ipa_words.csv")
word_dictionary = word_df.to_dict(orient="records")
current_word = ''
flip_timer = False
# ---------------------------- EVENT ---------------------------------- #

def on_closing():
    # Save the remaining words to learn
    df = pandas.DataFrame(word_dictionary)
    df.to_csv("data/word_to_learn.csv", index=False)
    window.destroy()
def next_word_event():
    global current_word, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)

    current_word = random.choice(word_dictionary)
    card_front_canvas.delete("all")
    card_front_canvas.create_image(400, 263, image=card_front_image)
    card_front_canvas.create_text(400, 150, text="English", font=("Ariel", 40))
    card_front_canvas.create_text(400, 263, text=current_word["English"], font=("Ariel", 60))
    # fliping card after 3 seconds 
    flip_timer = window.after(3000, flip_word_event)

def flip_word_event():
    card_front_canvas.delete("all")
    card_front_canvas.create_image(400, 263, image=card_back_image)
    card_front_canvas.create_text(400, 150, text="IPA Pronunciation", fill='#FFFFFF', font=("Ariel", 40))
    card_front_canvas.create_text(400, 263, text=current_word["IPA"], fill='#FFFFFF', font=("Ariel", 60))

def tick_word_event():
    next_word_event()
    global count, count_label
    count += 1
    count_label.config(text="Count of words learned today: " + str(count))
    if current_word != '':
        word_dictionary.remove(current_word)
    
def cross_word_event():
    next_word_event()

# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards") 
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=tick_word_event,  highlightthickness=0)
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
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
