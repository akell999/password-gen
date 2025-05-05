import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(password_length_entry.get())
        if not 8 <= length <= 20:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number between 8 and 20.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    password_entry.config(state="normal") 
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")  

def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200")  

instructions_label = tk.Label(window, text="Enter desired password length (8-20):")
instructions_label.pack(pady=5)

password_length_entry = tk.Entry(window)
password_length_entry.insert(0, "12")
password_length_entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_entry = tk.Entry(window, width=40, font=("Courier", 10))
password_entry.pack(pady=5)
password_entry.config(state="readonly") 

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_password)
copy_button.pack(pady=5)

window.mainloop()

