import tkinter as tk
import csv

def write_name_to_csv():
    with open('names.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name_entry.get()])
        name_entry.delete(0, 'end')

window = tk.Tk()
window.title("Name Input")
window.geometry("500x300")

name_label = tk.Label(window, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

submit_button = tk.Button(window, text="Submit", command=write_name_to_csv)
submit_button.pack()

window.mainloop()
