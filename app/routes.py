from flask import render_template
from app import app
from src import *


@app.route('/')
@app.route('/index')
def index():
    stock_request.stock_request("AAPL")
    reddit_requests.reddit_request("AAPL")
    return render_template('plot.html')