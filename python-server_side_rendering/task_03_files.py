#!/usr/bin/python3
"""Flask application to display product data from JSON and CSV files"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_data(file_path):
    """Read and parse data from a JSON file"""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_data(file_path):
    """Read and parse data from a CSV file"""
    products = []
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id to int and price to float for consistent data types
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
        return products
    except FileNotFoundError:
        return []


@app.route('/')
def home():
    """Route for the home page"""
    return render_template('index.html')


@app.route('/products')
def products():
    """
    Route to display products from JSON or CSV file
    Query parameters:
        - source: 'json' or 'csv' (required)
        - id: product ID to filter (optional)
    """
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Convert product_id to int if provided
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', 
                                  error="Invalid product ID")
    
    # Check if source is valid
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                              error="Wrong source")
    
    # Read data from the appropriate file
    if source == 'json':
        products_data = read_json_data('products.json')
    else:  # source == 'csv'
        products_data = read_csv_data('products.csv')
    
    # Filter by ID if provided
    if product_id:
        filtered_products = [p for p in products_data if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html', 
                                  error="Product not found")
        products_data = filtered_products
    
    # Render the template with the products data
    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True)
