from flask import render_template, redirect, url_for
from app.forms import StockForm
from app import app
from src import *


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = StockForm()
    if form.validate_on_submit():
        return redirect(url_for('display', id=form.stock.data))
    return render_template('index.html', title='Stock Analysis', form=form)


@app.route('/display/<id>', methods=['GET', 'POST'])
def display(id):
    stock_request.stock_request(id)
    reddit_requests.reddit_request(id)
    return render_template('plot.html')
