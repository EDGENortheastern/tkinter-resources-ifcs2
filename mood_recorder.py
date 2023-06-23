import tkinter as tk
from datetime import datetime
import csv
import os

# Function to write name, mood and current date to CSV
def write_to_csv():
    name = name_entry.get()
    mood = mood_entry.get()
    now = datetime.now().strftime('%Y-%m-%d')
    with open('names_and_moods.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, now, mood])
    name_entry.delete(0, 'end')
    mood_entry.delete(0, 'end')

# Check if CSV file exists and write headers if not
if not os.path.isfile('names_and_moods.csv'):
    with open('names_and_moods.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Date', 'Mood'])

# Create application window
window = tk.Tk()
window.geometry("500x400")
window.configure(bg='#FF77FF')

# Frame for name and mood entry
entry_frame = tk.Frame(window, bg='#FF77FF')
entry_frame.pack(pady=20)

# Entry for name
name_entry = tk.Entry(entry_frame, font=('Helvetica', 18), width=30)
name_entry.pack(pady=10)

# Entry for mood
mood_entry = tk.Entry(entry_frame, font=('Helvetica', 18), width=30)
mood_entry.pack(pady=10)

# Button to submit
submit_button = tk.Button(window, text="Submit", command=write_to_csv, bg='#FF77FF', font=('Helvetica', 18))
submit_button.pack(pady=10)

# Start Tkinter event loop
window.mainloop()



