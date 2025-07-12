from tkinter import *
from tkinter import messagebox
import pyperclip
import json
from json.decoder import JSONDecodeError  # <-- Added to catch JSON decode errors

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    import random

    letters = [*"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    numbers = [str(i) for i in range(10)]
    symbols = list('!#$%&()*+')

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_chars = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)]
    )
    random.shuffle(password_chars)

    password = ''.join(password_chars)
    password_entry.delete(0, END)  # <-- Clear existing entry before inserting
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().strip()       # <-- .strip() to remove extra spaces
    email = email_entry.get().strip()           # <-- .strip() added
    password = password_entry.get().strip()

    # <-- Warn if mandatory fields are empty
    if not website or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave Website or Password empty.")
        return

    new_data = {website: {"email": email, "password": password}}

    # Load existing data with error handling for missing or corrupt file
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        data = {}  # <-- Initialize empty dict if file not found or JSON invalid

    # Update and save
    data.update(new_data)
    try:
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Failed to save data: {e}")
    else:
        website_entry.delete(0, END)            # <-- Clear fields after successful save
        password_entry.delete(0, END)
        messagebox.showinfo(title="Success", message="Password saved successfully!")

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().strip()       # <-- .strip() added
    if not website:
        messagebox.showwarning(title="Oops", message="Please enter a website to search.")
        return

    # Attempt to load data, handle missing/corrupt file
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        messagebox.showinfo(title="No Data", message="No data file found.")
        return

    credentials = data.get(website)
    if credentials:
        messagebox.showinfo(
            title=website,
            message=f"Email: {credentials['email']}\nPassword: {credentials['password']}"
        )
    else:
        messagebox.showinfo(title="Not Found", message=f"No details for '{website}' found.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "devansh.khandar@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
Button(text="Search", width=13, command=find_password).grid(row=1, column=2)
Button(text="Generate Password", width=14, command=generate_password).grid(row=3, column=2)
Button(text="Add", width=30, command=save_password).grid(row=4, column=1, columnspan=2)

window.mainloop()
