import sqlite3

# Connect to a new database (or create it if it doesn't exist)
conn = sqlite3.connect('recipe.db')
cursor = conn.cursor()

# Create tables if they do not exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS recipe (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY,
    cocktail_id INTEGER,
    ingredient TEXT NOT NULL,
    FOREIGN KEY (cocktail_id) REFERENCES recipe (id)
)
''')

# Insert sample data
cursor.execute("INSERT INTO recipe (name) VALUES ('Margarita')")
recipe_id = cursor.lastrowid  # Get the last inserted id

ingredients = [('Tequila', recipe_id), ('Triple sec', recipe_id), ('Lime juice', recipe_id)]
cursor.executemany('INSERT INTO ingredients (ingredient, cocktail_id) VALUES (?, ?)', ingredients)

conn.commit()
conn.close()


