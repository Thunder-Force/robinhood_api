import pandas as pd

import robin_stocks.helper as helper
import robin_stocks.urls as urls


class Trader():
    def __init__(self, stocks):
        #self.buffer = 0.05
        self.run_time = 0
        self.stocks = stocks
        self.sma_hour = {stocks[i]: 0 for i in range(0, len(stocks))}
        self.sma_price_hour = {stocks[i]: 0 for i in range(0, len(stocks))}
        
    def get_stock_price_hist(self, stock, span):
        span_interval = {'5min','10min','30min','hour','day','week','month','year'}
        interval = span_interval(span)

        symbols = helper.inputs_to_set(stock)
        url = urls.historicals()

        payload = {
            'symbols': ','.join(symbols),
            'interval': interval,
            'span': span,
            'bounds': 'regular'
        }

        data = helper.requests_get(url,'results',payload)

        historical_data = []
        for item in data:
            for subitem in item['historicals']:
                    historical_data.append(subitem)

        df = pd.Dataframe(historical_data)

        print(f'\n[Data]:\n{df}')
        
