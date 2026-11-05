
import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Tkinter - Karma Yangchen")
window.geometry("500x350")
window.configure(bg="white")

# Function to handle button click
def show_message():
    messagebox.showinfo(
        "Welcome",
        "Hello! Welcome to my Tkinter application."
    )

# Display the heading
heading = tk.Label(
    window,
    text="Hello Everyone!",
    font=("Arial", 24, "bold"),
    fg="#4169E1",
    bg="white"
)
heading.pack(pady=25)

# Display a welcome message
message = tk.Label(
    window,
    text="My First Tkinter GUI Application",
    font=("Arial", 13),
    fg="#263238",
    bg="white"
)
message.pack(pady=10)

# Create an interactive button
hello_button = tk.Button(
    window,
    text="Click Me",
    font=("Arial", 12, "bold"),
    bg="#4169E1",
    fg="white",
    padx=20,
    pady=8,
    command=show_message
)
hello_button.pack(pady=15)

# Display student information
student_info = tk.Label(
    window,
    text="Karma Yangchen | Student ID: 08230137 | IT A | Roll No: 6",
    font=("Arial", 10),
    fg="#263238",
    bg="white"
)
student_info.pack(pady=15)

# Start the application
window.mainloop()
