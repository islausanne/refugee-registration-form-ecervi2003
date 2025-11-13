from flask import Flask
import os
import json
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Homepage!"



@app.route('/contact')
def contact():
    return "Contact us at: info@example.com."

if __name__ == '__main__':
    app.run(debug=True)
