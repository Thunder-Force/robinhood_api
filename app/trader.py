import config
import datetime as dt
import os
import pandas as pd
import robin_stocks.robinhood as rh
import robin_stocks.helper as helper
import robin_stocks.urls as urls
from app.terminal import Display 

class Trader():
    def __init__(self, stocks:list):
        self.display = Display()

        #self.buffer = 0.05
        self.run_time = 0
        self.stocks = stocks
        self.sma_hour = {stocks[i]: 0 for i in range(0, len(stocks))}
        self.sma_price_hour = {stocks[i]: 0 for i in range(0, len(stocks))}

        self.root_path = os.getcwd()
        self.data_path = f'{self.root_path}\\data'


    # LOGIN
    #================================================
    def login(self, auth_code):
        self.display.intro()
        try:
            login = rh.authentication.login(
                username = config.USERNAME, 
                password = config.PASSWORD,
                expiresIn = config.EXPIRATION, 
                scope = 'internal',
                store_session = True,
                mfa_code = auth_code
            )
        except Exception as ex:
            print(f'\nOops, something happened!\n Wrong MFA code maybe?\n\n[Error]: {ex}')
        else:
            print(f'>>> Trader logged in successfully.')


    # LOGOUT
    #================================================
    def logout(self):
        logout = rh.authentication.logout()
        print('>>> Trader logged out.')


    # IS MARKET OPEN 
    #================================================
    def is_market_open(self):
        market = False
        current_time = dt.datetime.now().time()
        market_open_time = dt.time(7,30,0)
        market_close_time = dt.time(13,59,0)
        
        if (current_time > market_open_time) and (current_time < market_close_time):
            market = True
            print('>>> Market is open.')
        else: 
            print('>>> Market is closed.')
        return True #market


    # GET STOCK PRICES
    #================================================
    def get_stock_prices(self):
        for ticker in self.stocks:
            r = rh.stocks.get_latest_price(ticker)
            print(f'{ticker.upper()}:  ${r[0]}')


    # GET STOCK PRICES HIST
    #================================================
    def get_stock_prices_hist(self, stock, interval, span):
        hist_data = rh.stocks.get_stock_historicals( stock, interval, span, bounds='extended')
        df = pd.DataFrame(hist_data)
        df.to_csv(f'{self.data_path}\\{stock}.csv')

        print(f'\n[Data]:\n{df.head()}')



    # GET STOCK PRICES HIST
    #================================================
    def trigger_automation(self):
        interval = ['5minute', '10minute', 'hour', 'day', 'week']
        span = ['day', 'week', 'month', '3month', 'year', '5year']

        self.get_stock_prices()

        for stock in self.stocks:
            # keep the indexes together
            self.get_stock_prices_hist(stock, interval[0], span[0])
