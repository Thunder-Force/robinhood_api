
class Display():
    def intro(self):
        i  = '======================================\n'
        i += '==      Stock Market AI BOT        ===\n'
        i += '==         by Mitch Alves          ===\n'       
        i += '======================================\n'
        return print(i)

    def market_open(self):
        o  = '======================================\n'
        o += '==           MARKET OPEN           ===\n'       
        o += '======================================\n'
        return print(o)

    def market_close(self):
        c  = '======================================\n'
        c += '==          MARKET CLOSED          ===\n'       
        c += '======================================\n'
        return print(c) 