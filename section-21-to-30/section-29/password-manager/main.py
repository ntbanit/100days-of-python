from tkinter import *
from tkinter import messagebox
import random
import string

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

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, 
                                       message=f"These are the details entered: \nEmail: {username} "
                                               f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
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
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0, "ntbanit@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="W")

generate_button = Button(text="Generate Password", command=generate_password, width=15)
generate_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", command=add_password, width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
window.mainloop()
# ---------------------------- END UI SETUP ------------------------------- #
