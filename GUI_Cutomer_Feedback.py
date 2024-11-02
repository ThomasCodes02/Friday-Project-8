import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to handle the submit button click
def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get("1.0", tk.END)  # Retrieve multi-line text
    
    # Basic validation
    if not name or not email or not feedback.strip():
        messagebox.showerror("Input Error", "All fields are required!")
        return
    
    # Insert feedback into the database
    try:
        conn = sqlite3.connect('customer_feedback.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (name, email, message) VALUES (?, ?, ?)",
                       (name, email, feedback.strip()))
        conn.commit()
        conn.close()
        
        # Clear the fields after submission
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_feedback.delete("1.0", tk.END)
        
        messagebox.showinfo("Success", "Thank you for your feedback!")
        
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")

# Set up the main application window
app = tk.Tk()
app.title("Customer Feedback Form")
app.geometry("400x300")

# Create and place the Name label and entry
tk.Label(app, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_name = tk.Entry(app, width=40)
entry_name.grid(row=0, column=1, padx=10, pady=10)

# Create and place the Email label and entry
tk.Label(app, text="Email").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(app, width=40)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Create and place the Feedback label and entry
tk.Label(app, text="Feedback").grid(row=2, column=0, padx=10, pady=10, sticky="nw")
entry_feedback = tk.Text(app, width=30, height=5)
entry_feedback.grid(row=2, column=1, padx=10, pady=10)

# Create and place the Submit button
submit_button = tk.Button(app, text="Submit", command=submit_feedback)
submit_button.grid(row=3, column=1, pady=20)

# Run the application
app.mainloop()
