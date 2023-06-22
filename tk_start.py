# Import the Tkinter library for GUI creation
import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()

# Set the title of the window to "Hello world"
window.title("Hello world")

# Set the size of the window to be 500 pixels wide and 100 pixels tall
window.geometry("500x400")

# Set the background color of the window to light fuchsia
window.configure(bg='#FF77FF')

# Creates a new label 👇

hello = tk.Label(window, text="Hello world!", fg='#006400', bg='#FF77FF', font=('Helvetica', 18, 'bold'))

# The place() method places the label in a specific place.👇

hello.place(relx=0.5, rely=0.5, anchor='center')

# the Tkinter event loop 👇

tk.mainloop()