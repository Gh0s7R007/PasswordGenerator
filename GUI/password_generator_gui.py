# password_gui.py
import tkinter as tk
from tkinter import messagebox, filedialog
from password_generator import generate_password, password_strength

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_numbers = numbers_var.get()
        use_special = special_var.get()

        if length < 8 or length > 32:
            messagebox.showerror("Error", "Length must be between 8 and 32.")
            return

        password = generate_password(length, use_upper, use_lower, use_numbers, use_special)
        strength, score = password_strength(password)

        password_label.config(text=f"Generated Password: {password}")
        strength_label.config(text=f"Strength: {strength} (Score: {score:.2f}%)")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length.")

def export_password():
    password = password_label.cget("text").replace("Generated Password: ", "")
    if not password or password == "Generated Password: ":
        messagebox.showerror("Error", "No password to export.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(password)
        messagebox.showinfo("Success", "Password exported successfully!")

# Set up the GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#f0f0f0")
root.iconbitmap('image.ico')

# Title
title = tk.Label(root, text="Choose your parameters", font=("Helvetica", 16, "bold"), bg="#282c34", fg="#ffffff")
title.pack(pady=10)

# Length input
tk.Label(root, text="Password Length (8-32):", bg="#f0f0f0").pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

# Options for character types
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var, bg="#f0f0f0").pack(anchor='w')
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var, bg="#f0f0f0").pack(anchor='w')
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, bg="#f0f0f0").pack(anchor='w')
tk.Checkbutton(root, text="Include Special Characters", variable=special_var, bg="#f0f0f0").pack(anchor='w')

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, bg="#4CAF50", fg="white", font=("Arial", 12))
generate_button.pack(pady=10)

# Labels to display the password and strength
password_label = tk.Label(root, text="Generated Password: ", bg="#f0f0f0", wraplength=350)
password_label.pack(pady=5)

strength_label = tk.Label(root, text="Strength: ", bg="#f0f0f0")
strength_label.pack(pady=5)

# Export button
export_button = tk.Button(root, text="Export Password", command=export_password, bg="#2196F3", fg="white", font=("Arial", 12))
export_button.pack(pady=10)

# Run the application
root.mainloop()