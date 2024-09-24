from flask import Flask, jsonify, render_template, request
from models import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/lotInfo')
def lot():
    return render_template('lot.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/api/register', methods=['GET'])
def register():
    pass

@app.route('/api/login', methods=['GET'])
def login():
    pass

@app.route('/api/createLots', methods=['GET'])
def createLots():
    pass

@app.route('/api/getLots', methods=['POST'])
def getLots():
    pass

if __name__ == '__main__':
    app.run('0.0.0.0')