import sqlite3

# Read SQL data from a file
with open('recipe.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

# Connect to SQLite database (or create it)
conn = sqlite3.connect('recipe.db')
cursor = conn.cursor()

# Execute SQL script to create tables and insert data
cursor.executescript(sql_script)

# Query the cocktail data to verify insertion
cursor.execute('SELECT * FROM recipe')
cocktails = cursor.fetchall()


# Commit changes and close connection
conn.commit()
conn.close()

print("Data loaded successfully from SQL file into SQLite database.")
