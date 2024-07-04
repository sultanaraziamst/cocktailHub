import sqlite3
import pandas as pd
from flask import Flask, render_template, request
import json

# Connect to SQLite database
conn = sqlite3.connect('recipes.db')


app = Flask(__name__)

def get_cocktail_recipe(cocktail_name):
    """Function to retrieve ingredients for a given cocktail name."""
    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()

    # Perform a case insensitive search for the cocktail name
    cursor.execute('''
        SELECT ingredient
        FROM recipes
        WHERE ingredients = (SELECT Garnish FROM recipe WHERE LOWER(name) = LOWER(?))
    ''', (cocktail_name,))
    
    ingredients = cursor.fetchall()

    conn.close()

    return [ingredient[0] for ingredient in ingredients] if ingredients else None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.data)
        print(request.form)
        cocktail_name = request.form['cocktail_name'].strip()
        recipes = get_cocktail_recipe(cocktail_name)
        return render_template('index.html', cocktail_name=cocktail_name, ingredient=recipe)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


