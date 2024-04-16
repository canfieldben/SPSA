import datetime
today = datetime.date.today()
last_month = today - datetime.timedelta(days=31)
print(last_month.strftime("%Y-%m-%d"))