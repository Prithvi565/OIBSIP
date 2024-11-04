import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random
import string
import pyperclip


def password():
    length = Len.get()
    
    if length < 6:
        messagebox.showwarning("Warning", "Password length should be at least 6 characters!")
        return
    
    charset = ''
    
    if lowercase_var.get():
        charset += string.ascii_lowercase
    if uppercase_var.get():
        charset += string.ascii_uppercase
    if digits_var.get():
        charset += string.digits
    if special_var.get():
        charset += string.punctuation

    if not charset:
        messagebox.showinfo("Info", "Please select at least one character set!")
        return

    password = []
    if lowercase_var.get():
        password.append(random.choice(string.ascii_lowercase))
    if uppercase_var.get():
        password.append(random.choice(string.ascii_uppercase))
    if digits_var.get():
        password.append(random.choice(string.digits))
    if special_var.get():
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(charset))

    random.shuffle(password)
    password = ''.join(password)

    passwd_entry.delete(0, tk.END)
    passwd_entry.insert(0, password)

def copy():
    password = passwd_entry.get()
    if password:
        pyperclip.copy(password)
        msg = tk.Label(window, text="copied!", bg="#263238", fg="#ffffff")
        msg.pack()
        window.after(2000, msg.destroy)
    else:
        msg = tk.Label(window, text="Password not generated yet", bg="#263238", fg="#ffffff")
        msg.pack()
        window.after(2000, msg.destroy)

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x260")
window.config(bg='#263238')

Len = tk.IntVar(value=12)
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Label(window, text="Password Length:", bg="#263238", fg="#eceff1").pack(pady=10)
spinbox_bg = "#cfd8dc"
tk.Spinbox(window, from_=6, to_=50, textvariable=Len, width=5, bg=spinbox_bg, fg="#000000", borderwidth=2).pack()

f = tk.Frame(window, bg="#263238")
f.pack(pady=5)
tk.Checkbutton(f, text="Lowercase", variable=lowercase_var, bg="#263238", fg="#eceff1", selectcolor="#546e7a").pack(side='left')
tk.Checkbutton(f, text="Uppercase", variable=uppercase_var, bg="#263238", fg="#eceff1", selectcolor="#546e7a").pack(side='left')
tk.Checkbutton(f, text="Digits", variable=digits_var, bg="#263238", fg="#eceff1", selectcolor="#546e7a").pack(side='left')
tk.Checkbutton(f, text="Special Characters", variable=special_var, bg="#263238", fg="#eceff1", selectcolor="#546e7a").pack(side='left')

tk.Label(window, text="Generated Password:", bg="#263238", fg="#eceff1").pack(pady=10)
passwd_entry = tk.Entry(window, width=30, font=('Arial', 12), bg="#37474f", fg="#eceff1")
passwd_entry.pack()

tk.Button(window, text="Generate Password", bg="#cfd8dc", command=password).pack(pady=10)
tk.Button(window, text="Copy", bg="#cfd8dc", command=copy).pack(pady=5)

window.mainloop()
