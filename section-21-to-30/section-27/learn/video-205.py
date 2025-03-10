import tkinter 
window = tkinter.Tk()
window.title("My First GUI")
window.minsize(500, 300)

label = tkinter.Label(text="Hello, World!", font=("Arial", 24))
label.pack()
# label.config(text="Goodbye, World!")

def button_click():
    label.config(text="Button Clicked!")

button = tkinter.Button(text="Change Text", command=button_click)
button.pack()

entry = tkinter.Entry(width=30)
entry.pack()
# get the text from the entry
def entry_click():
    user_text = entry.get()
    label.config(text=user_text)
entry_button = tkinter.Button(text="Get Text", command=entry_click)
entry_button.pack()

window.mainloop()