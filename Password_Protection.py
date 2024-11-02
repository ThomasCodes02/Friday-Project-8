import tkinter as tk
from tkinter import messagebox
import sqlite3

# Define the admin password
ADMIN_PASSWORD = "123"

# Function to handle feedback submission
def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get("1.0", tk.END)
    
    if not name or not email or not feedback.strip():
        messagebox.showerror("Input Error", "All fields are required!")
        return
    
    try:
        conn = sqlite3.connect('customer_feedback.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (name, email, message) VALUES (?, ?, ?)", 
                       (name, email, feedback.strip()))
        conn.commit()
        conn.close()
        
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_feedback.delete("1.0", tk.END)
        
        messagebox.showinfo("Success", "Thank you for your feedback!")
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")

# Function to retrieve and display feedback with password protection
def retrieve_feedback():
    # Prompt for password in the console
    password = input("Enter admin password to view feedback: ")
    
    if password == ADMIN_PASSWORD:
        try:
            conn = sqlite3.connect('customer_feedback.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM feedback")
            records = cursor.fetchall()
            conn.close()
            
            if records:
                print("\nCustomer Feedback:")
                print("ID | Name | Email | Feedback")
                print("-" * 40)
                for record in records:
                    print(f"{record[0]} | {record[1]} | {record[2]} | {record[3]}")
            else:
                print("No feedback entries found.")
        except Exception as e:
            print(f"An error occurred while retrieving feedback: {e}")
    else:
        print("Access denied. Incorrect password.")

# GUI setup
app = tk.Tk()
app.title("Customer Feedback Form")
app.geometry("400x350")

tk.Label(app, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_name = tk.Entry(app, width=40)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Email").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(app, width=40)
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Feedback").grid(row=2, column=0, padx=10, pady=10, sticky="nw")
entry_feedback = tk.Text(app, width=30, height=5)
entry_feedback.grid(row=2, column=1, padx=10, pady=10)

submit_button = tk.Button(app, text="Submit", command=submit_feedback)
submit_button.grid(row=3, column=1, pady=10)

# Add "Retrieve Feedback" button to trigger the password-protected data retrieval
retrieve_button = tk.Button(app, text="Retrieve Feedback", command=retrieve_feedback)
retrieve_button.grid(row=4, column=1, pady=10)

app.mainloop()
