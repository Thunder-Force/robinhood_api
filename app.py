
from trader import Trader

MFA_CODE = '364295'
STOCKS = ['DNUT']


if __name__ == '__main__':
    trader = Trader(STOCKS)
    trader.login(MFA_CODE)  
    trader.is_market_open()
    trader.trigger_automation()
    trader.logout()