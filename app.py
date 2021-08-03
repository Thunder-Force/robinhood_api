from robinhood import Robinhood

# CONFIG
#=======================================================
MFA_CODE = 442155
STOCKS = ['aapl', 'dnut']


# MAIN
#=======================================================
if __name__ == '__main__':

    bot = Robinhood()
    bot.login(MFA_CODE) 
    
    #while(bot.market_check()):
    bot.view_stock(STOCKS)
