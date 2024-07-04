import sqlite3
import json

DB_FILE = 'recipes.db'

def create_connection(db_file):
    """ Create a connection to SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database '{db_file}'")
    except sqlite3.Error as e:
        print(f"Error connecting to SQLite database '{db_file}': {e}")
    return conn

def create_table(conn):
    """ Create recipe table if not exists """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                glass TEXT,
                category TEXT,
                ingredients TEXT,
                garnish TEXT,
                recipe TEXT,
                preparation TEXT
            );
        ''')
        print("Table 'recipes' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_data(conn, data):
    """ Insert data into recipes table """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO recipes (name, glass, category, ingredients, garnish, preparation)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

def insert_json_data(conn, json_file):
    """ Insert data from JSON file into recipe table """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            recipes = json.load(f)
            for recipe in recipes:
                category = recipe.get('category', '')
                ingredients = json.dumps(recipe['ingredients'])
                insert_data(conn, (
                    recipe['name'],
                    recipe.get('glass'),
                    category,
                    ingredients,
                    recipe.get('garnish'),
                    recipe.get('preparation')
                ))
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file '{json_file}': {e}")

if __name__ == '__main__':
    conn = create_connection(DB_FILE)
    if conn is not None:
        create_table(conn)
        insert_json_data(conn, 'recipes.json')
        conn.close()
