from flask import Flask, jsonify, render_template, request
from models import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/api/activeLots', methods=['GET'])
def activeLots():
    pass

@app.route('/api/createLots', methods=['POST'])
def createLots():
    pass



if __name__ == '__main__':
    app.run('0.0.0.0')