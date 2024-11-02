import sqlite3

# Create Database Name
conn = sqlite3.connect('customer_feedback.db')

# Cursor
cursor = conn.cursor()

# Create the Table for Feedback
cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
