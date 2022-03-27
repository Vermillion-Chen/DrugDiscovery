import os
from unicodedata import name
from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = Flask(__name__, template_folder='./templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ ==  "__main__":
    app.run()