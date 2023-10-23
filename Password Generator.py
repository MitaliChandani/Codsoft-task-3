import tkinter as tk 
from tkinter import messagebox
import random
import string

def generate_password(length, complexity):
    characters = ""
    if complexity == "Low":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    if length < 1:
        messagebox.showerror("Try Again" , "Password length should be at least 1.")
        return
    if complexity not in ("Low", "Medium", "High"):
        messagebox.showerror("Invalid complexity level.")
        return
    password = generate_password(length, complexity)
    result_label.config(text="Generated Password: " + password)
    result_label.configure(bg="lightgreen")  

root = tk.Tk()
root.title("Password Generator")
root.geometry("200x200")  
root.configure(bg="navajo white")  

length_label = tk.Label(root, text="Password Length:", bg="navajo white")
length_label.pack()
length_entry = tk.Entry(root, width=20)
length_entry.pack()

complexity_label = tk.Label(root, text="Complexity Level:", bg="navajo white")
complexity_label.pack()

complexity_var = tk.StringVar()
complexity_var.set("Low")
complexity_low_radio = tk.Radiobutton(root, text="Low", variable=complexity_var, value="Low", width=15, bg="navajo white")
complexity_medium_radio = tk.Radiobutton(root, text="Medium", variable=complexity_var, value="Medium", width=15, bg="navajo white")
complexity_high_radio = tk.Radiobutton(root, text="High", variable=complexity_var, value="High", width=15, bg="navajo white")
complexity_low_radio.pack()
complexity_medium_radio.pack()
complexity_high_radio.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, width=20, bg="lightgreen", fg="black")
generate_button.pack()

result_label = tk.Label(root, text="", width=40, bg="lightyellow")
result_label.pack()

root.mainloop()