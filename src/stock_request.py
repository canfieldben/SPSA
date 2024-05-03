from polygon import RESTClient
import datetime as dt
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
import os

# gets directory for html files
dir = os.getcwd()
parDir = os.path.dirname(os.getcwd())

# PRAW API keys
polygonAPIkey = "CMpQPwZecYoKyqM5Lt8ygrafXMhUgpSj"
client = RESTClient(polygonAPIkey)


def stock_request(stockTicker):
    today = dt.date.today()  # today's date
    last_month = today - dt.timedelta(days=31)  # calculate a month ago
    last_month = last_month.strftime("%Y-%m-%d")  # format the date

    one_year = '2023-04-23'

    # stock API request
    dataRequest = client.get_aggs(ticker=stockTicker,
                                  multiplier=1,
                                  timespan='day',
                                  from_=last_month,
                                  to='2100-01-01')

    priceData = pd.DataFrame(dataRequest)  # add data to a dataframe

    # datetime formatting
    priceData['Date'] = priceData['timestamp'].apply(
        lambda x: pd.to_datetime(x * 1000000))

    priceData = priceData.set_index('Date')

    # plot the dataframe with market prices
    fig = go.Figure(data=[go.Candlestick(x=priceData.index,
                                         open=priceData['open'],
                                         high=priceData['high'],
                                         low=priceData['low'],
                                         close=priceData['close'])])

    # writes plot to html file
    try:
        fig.write_html(f"{dir}/app/templates/plot.html")
    except:
        print("local test")
        plot(fig, auto_open=True)
        fig.write_html(f"{parDir}/app/templates/plot.html")

# stock_request("IBM")  # ONLY FOR TESTING PURPOSES. DOES NOT RUN WHEN RUNNING THROUGH FLASK APPLICATION
