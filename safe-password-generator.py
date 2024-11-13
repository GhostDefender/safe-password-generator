import random
import string
import tkinter as tk
from tkinter import ttk

# Function to generate a secure password
def generate_password(event=None):  # Add event parameter for Enter key binding
    try:
        length = int(length_entry.get())
        if length < 8:
            result_label.config(text="Password length must be at least 8.", fg="red")
            return
        elif length > 250:
            result_label.config(text="Password length cannot exceed 250.", fg="red")
            return
    except ValueError:
        result_label.config(text="Please enter a valid number.", fg="red")
        return
    
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all characters
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure that there is at least one of each type of character
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password with random characters
    password += [random.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the characters to make the password less predictable
    random.shuffle(password)

    # Join the list of characters into a string and display it
    generated_password = ''.join(password)
    result_label.config(text=f"Generated Password: {generated_password}", fg="green")

# Setting up the main Tkinter window
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x200")

# Label and Entry for password length
length_label = ttk.Label(root, text="Enter password length (minimum 8, maximum 250):")
length_label.pack(pady=10)

length_entry = ttk.Entry(root)
length_entry.pack(pady=5)
length_entry.bind("<Return>", generate_password)  # Bind Enter key to generate_password function

# Button to generate password
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Using tk.Label instead of ttk.Label for color functionality
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()