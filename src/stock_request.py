from polygon import RESTClient
import datetime as dt
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
import os

dir = os.getcwd()
parDir = os.path.dirname(os.getcwd())

polygonAPIkey = "CMpQPwZecYoKyqM5Lt8ygrafXMhUgpSj"
client = RESTClient(polygonAPIkey)


def stock_request(stockTicker):
    today = dt.date.today()
    last_month = today - dt.timedelta(days=31)
    last_month = last_month.strftime("%Y-%m-%d")

    one_year = '2023-04-23'

    dataRequest = client.get_aggs(ticker=stockTicker,
                                  multiplier=1,
                                  timespan='day',
                                  from_=last_month,
                                  to='2100-01-01')

    priceData = pd.DataFrame(dataRequest)

    priceData['Date'] = priceData['timestamp'].apply(
        lambda x: pd.to_datetime(x * 1000000))

    priceData = priceData.set_index('Date')

    fig = go.Figure(data=[go.Candlestick(x=priceData.index,
                                         open=priceData['open'],
                                         high=priceData['high'],
                                         low=priceData['low'],
                                         close=priceData['close'])])

    try:
        fig.write_html(f"{dir}/app/templates/plot.html")
    except:
        print("local test")
        plot(fig, auto_open=True)
        fig.write_html(f"{parDir}/app/templates/plot.html")


# stock_request("IBM")  # ONLY FOR TESTING PURPOSES. DOES NOT RUN WHEN RUNNING THROUGH FLASK APPLICATION
