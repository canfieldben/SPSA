from importing_modules import *


polygonAPIkey = "CMpQPwZecYoKyqM5Lt8ygrafXMhUgpSj"

client = RESTClient(polygonAPIkey)

stockTicker = 'AAPL'

dataRequest = client.get_aggs(ticker = stockTicker,
                              multiplier = 1,
                              timespan = 'day',
                              from_ = '2022-09-01',
                              to = '2100-01-01')

priceData = pd.DataFrame(dataRequest)

priceData['Date'] = priceData['timestamp'].apply(
                          lambda x: pd.to_datetime(x*1000000))

priceData = priceData.set_index('Date')

fig = go.Figure(data=[go.Candlestick(x=priceData.index,
                open=priceData['open'],
                high=priceData['high'],
                low=priceData['low'],
                close=priceData['close'])])

# plot(fig, auto_open=True)
fig.write_html("C:/Users/bcanf/Documents/GitHub/SPSA/app/templates/plot.html")