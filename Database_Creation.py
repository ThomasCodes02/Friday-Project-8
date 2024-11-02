import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect('customer_feedback.db')

# Create a cursor to interact with the database
cursor = conn.cursor()

# SQL command to create the feedback table
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
