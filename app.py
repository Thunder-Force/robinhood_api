from terminal import Display 
from trader import Trader
from robinhood import Robinhood
import time

# INIT
#=======================================================
MFA_CODE = 244461
STOCKS = ['aapl', 'dnut']

dp = Display()
bot = Robinhood()
trader = Trader()

# MAIN
#=======================================================
if __name__ == '__main__':

    dp.intro()
    try:
        bot.login(MFA_CODE) 
    except Exception as ex:
        print(f'Oops, something happened!\n MFA code maybe?\n\n[Error]: {ex}')

    while(bot.stock_check()):
        bot.stock_check(STOCKS)

        time.sleep(60)