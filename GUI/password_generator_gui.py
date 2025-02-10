# password_gui.py
import tkinter as tk
from tkinter import messagebox, filedialog
from password_generator_module import generate_password, password_strength

# Global list to store password history
password_history = []

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

        # Update password history
        password_history.append(password)

        password_label.config(text=f"Generated Password: {password}")
        strength_label.config(text=f"Strength: {strength} (Score: {score:.2f}%)")
        update_history_display()
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length.")

def update_history_display():
    history_text.delete(1.0, tk.END)  # Clear previous history
    for pwd in password_history:
        history_text.insert(tk.END, pwd + "\n")

def copy_to_clipboard():
    password = password_label.cget("text").replace("Generated Password: ", "")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def export_history():
    if not password_history:
        messagebox.showerror("Error", "No history to export.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            for pwd in password_history:
                file.write(pwd + "\n")
        messagebox.showinfo("Success", "History exported successfully!")

# Set up the GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("700x450")  # Landscape window
root.configure(bg="#f0f0f0")

# Title
title = tk.Label(root, text="Password Generator", font=("Helvetica", 20, "bold"), bg="#282c34", fg="#ffffff")
title.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# Length input
tk.Label(root, text="Password Length (8-32):", bg="#f0f0f0").grid(row=1, column=0, sticky='w', padx=10, pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.grid(row=1, column=1, padx=10, pady=5)

# Options for character types
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var, bg="#f0f0f0").grid(row=2, column=0, sticky='w', padx=10)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var, bg="#f0f0f0").grid(row=3, column=0, sticky='w', padx=10)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, bg="#f0f0f0").grid(row=4, column=0, sticky='w', padx=10)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var, bg="#f0f0f0").grid(row=5, column=0, sticky='w', padx=10)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10)
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Labels to display the password and strength
password_label = tk.Label(root, text="Generated Password: ", bg="#f0f0f0", wraplength=350)
password_label.grid(row=7, column=0, columnspan=2, pady=5)

strength_label = tk.Label(root, text="Strength: ", bg="#f0f0f0")
strength_label.grid(row=8, column=0, columnspan=2, pady=5)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white", font=("Arial", 12))
copy_button.grid(row=9, column=0,columnspan=2, pady=10)

# History display
history_frame = tk.Frame(root, bg="#f0f0f0")
history_frame.grid(row=1, column=2, rowspan=8, padx=10, pady=10)

tk.Label(history_frame, text="Password History:", bg="#f0f0f0").pack(side=tk.TOP)
history_text = tk.Text(history_frame, height=15, width=40, wrap=tk.WORD)
history_text.pack(side=tk.LEFT, padx=5)

# Position the export button below the history frame
export_button = tk.Button(root, text="Export History", command=export_history, bg="#FF9800", fg="white", font=("Arial", 12))
export_button.grid(row=9, column=2, pady=10)

# Run the application
root.mainloop()