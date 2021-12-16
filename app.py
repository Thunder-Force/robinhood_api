from terminal import Display 
from trader import Trader
from robinhood import Robinhood
import time

# INIT
#=======================================================
MFA_CODE = '057671'
STOCKS = ['aapl', 'dnut']

dp = Display()
bot = Robinhood()
trader = Trader(STOCKS)

# MAIN
#=======================================================
if __name__ == '__main__':

    dp.intro()
    try:
        bot.login(MFA_CODE) 
    except Exception as ex:
        print(f'Oops, something happened!\n MFA code maybe?\n\n[Error]: {ex}')
    

    while(bot.market_check()):
        prices = bot.stock_check(STOCKS)

        for i, stock in enumerate(STOCKS):
            price = float(prices[i])
            print('{} = ${}'.format(stock,price))

            data = trader.get_stock_price_hist(stock, span='days')


        time.sleep(30)

    bot.logout()