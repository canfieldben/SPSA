from flask import render_template, redirect, url_for
from app.forms import StockForm
from app import app
from src import stock_request, reddit_requests


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = StockForm()
    if form.validate_on_submit():
        return redirect(url_for('display', id=form.stock.data, company=form.company.data))
    return render_template('index.html', title='Stock Analysis', form=form)


@app.route('/display/<id>/<company>', methods=['GET', 'POST'])
def display(id, company):
    stock_request.stock_request(id)
    reddit_requests.reddit_request(company)
    return render_template('plot.html')
