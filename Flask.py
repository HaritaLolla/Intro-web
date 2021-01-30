from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

# this should return an error
@app.route('/test')
def test():
    return render_template('test.html')
	
@app.route('/index')
def index():
    return render_template('index.html')
	
@app.route('/mywebsite')
def mywebsite():
    return render_template('first.html')

@app.route('/add')
def add():

	x = 5 
	y = 4 
    t = datetime.time(datetime.now())
    return x+y, t 

app.run(port=8080)