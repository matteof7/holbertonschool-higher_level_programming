#!/usr/bin/python3
"""Flask application with dynamic content using Jinja templates"""
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    """Route for the home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """Route for the about page"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Route for the contact page"""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Route for the items page that displays items from JSON file"""
    try:
        # Open and read the JSON file
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        # If file not found or invalid JSON, use empty list
        items_list = []
    
    # Render the template with the items
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True)
