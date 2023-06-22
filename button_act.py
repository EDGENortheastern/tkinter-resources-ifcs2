import tkinter as tk
import random

def change_bg_color(): # gets random screen colors
    colors = ['#FF77FF', '#77FF77', '#7777FF', '#d415c7', '#1528d4']
    now_color = random.choice(colors)
    window.configure(bg=now_color)

window = tk.Tk()

# Set the title, size and starting background color of the window
window.title("Color Changer")
window.geometry("500x300")
window.configure(bg='#FF77FF')

# Create a button control

button = tk.Button(window, text="Change Color", fg='#000066', bg='#FFFF66', font=('Helvetica', 16, 'bold'), command=change_bg_color)
button.place(relx=0.5, rely=0.5, anchor='center')

tk.mainloop()
