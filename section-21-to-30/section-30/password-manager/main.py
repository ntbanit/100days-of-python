from tkinter import *
from tkinter import messagebox
import random
import string
import json

font_name=("Consolas", 8)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Generate a random password with 8->10 letters, 2->4 symbols, and 2->4 numbers
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # Copy password to clipboard
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()
# ---------------------------- SEARCH PASSWORD ----------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} found.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        messagebox.showerror(title="Error", message=f"Unable to read data.json: {e}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website :{
            "username": username,
            "password": password
        }
    }

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError) :
        with open("data.json", mode="w") as file:
            json.dump({}, file)
        data = {}

    data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    messagebox.showinfo(title="Success", message="Password saved successfully!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager") 
window.config(padx=20, pady=20)

canvas = Canvas( width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)
label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
label3 = Label(text="Password:")
label3.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

search_button = Button(text="Search", command=search_password, width=15)
search_button.grid(row=1, column=2, sticky="EW")

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0, "test@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="W")

generate_button = Button(text="Generate Password", command=generate_password, width=15)
generate_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", command=add_password, width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
window.mainloop()
# ---------------------------- END UI SETUP ------------------------------- #
