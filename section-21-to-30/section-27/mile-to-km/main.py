import tkinter 
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(200, 100)
window.config(padx=20, pady=20)

label1 = tkinter.Label(text="Miles")
label1.grid(row=0, column=2)
label2 = tkinter.Label(text="is equal to")
label2.grid(row=1, column=0)
label3 = tkinter.Label(text="km")
label3.grid(row=1, column=2)

km_label = tkinter.Label(text="0")
km_label.grid(row=1, column=1)

entry = tkinter.Entry(width=10)
entry.grid(row=0, column=1)

def caculate_miles():
    miles = entry.get()
    km = float(miles) * 1.60934
    km_label.config(text=f"{km:.2f}")
    
button = tkinter.Button(text="Caculate", command=caculate_miles)
button.grid(row=2, column=1)


window.mainloop()