import pandas as pandas
from alpha_vantage.timeseries import TimeSeries
import time

api_key = "PYLBXSESPITGYP8G"

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol= "MSFT", interval = "1min", outputsize= "full")

while True:
	data, meta_data = ts.get_intraday(symbol= "MSFT", interval = "1min", outputsize= "full")
	close_data = data['4. close']
	percentage_change = close_data.pct_change()

	print(percentage_change)

	last_change = percentage_change[-1]

	if abs(last_change) > 1.0000:
		print('MSFT Alert: ' + last_change)
	time.sleep(60)

