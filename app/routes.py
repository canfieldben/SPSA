from flask import render_template, redirect, url_for
from app.forms import StockForm
from app import app
from src import stock_request, reddit_requests


# main route for calculations
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = StockForm()
    if form.validate_on_submit():
        stock_request.stock_request(form.stock.data)
        reddit_requests.reddit_request(form.company.data)
        return redirect(url_for('display'))
    return render_template('index.html', title='Stock Analysis', form=form)


# only used for IFRAME
@app.route('/plot', methods=['GET', 'POST'])
def plot():
    return render_template('plot.html')


# only used for IFRAME
@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    return render_template('sentiment.html')


# container for IFRAME
@app.route('/display', methods=['GET', 'POST'])
def display():
    return render_template('charts.html')
