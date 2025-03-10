import tkinter 
window = tkinter.Tk()
window.title("My First GUI")
window.minsize(500, 300)
window.config(padx=10, pady=10)

label = tkinter.Label(text="Hello, World!")
label.grid(row=0, column=0)

button = tkinter.Button(text="Click Me", command=lambda: print("Button clicked!"))

button.grid(row=1, column=1)

new_button = tkinter.Button(text="New Button", command=lambda: print("New button clicked!"))

new_button.grid(row=0, column=2)

entry = tkinter.Entry(width=10)
entry.grid(row=2, column=3)

window.mainloop()