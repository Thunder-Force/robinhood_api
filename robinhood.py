import config
import datetime as dt
import robin_stocks.robinhood as rh

class Robinhood():
    def login(self, auth_code):
        login = rh.authentication.login(
            username = config.USERNAME, 
            password = config.PASSWORD,
            expiresIn = config.EXPIRATION, 
            scope = 'internal',
            store_session = True,
            mfa_code = auth_code
        )
        print('Logged in.')

    def logout(self):
        logout = rh.authentication.logout()
        print('Logged out.')

    def is_market_open(self):
        market = False
        current_time = dt.datetime.now().time()
        market_open_time = dt.time(7,30,0)
        market_close_time = dt.time(13,59,0)
        
        if (current_time > market_open_time) and (current_time < market_close_time):
            market = True
            print('Market is open.')
        else: 
            print('Market is closed.')
        return True#market

    def get_price(self, ticker_list):
        for ticker in ticker_list:
            r = rh.stocks.get_latest_price(ticker)
            print(f'{ticker.upper()}:  ${r[0]}')

        