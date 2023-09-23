import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Canyon!'

@app.route('/about')
def about():
    return 'About'

@app.route('/hello')
def hello():
    return 'its your boy!'

@app.route('/checksite')
def check_site():
    try:
        response = requests.get('https://cars.ksl.com/')
        return response.text
    except:
        return 'its not'