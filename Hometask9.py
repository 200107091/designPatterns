class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.investors = []

    def add_investor(self, investor):
        self.investors.append(investor)

    def remove_investor(self, investor):
        self.investors.remove(investor)

    def update_price(self, new_price):
        self.price = new_price
        self.notify_investors()

    def notify_investors(self):
        for investor in self.investors:
            investor.update(self)


class Investor:
    def __init__(self, name):
        self.name = name
        self.investments = []

    def add_investment(self, stock):
        self.investments.append(stock)
        stock.add_investor(self)

    def remove_investment(self, stock):
        self.investments.remove(stock)
        stock.remove_investor(self)

    def update(self, stock):
        print(f"{self.name} received an update for {stock.symbol} stock, new price: {stock.price}")



aapl_stock = Stock("AAPL", 150.0)
msft_stock = Stock("MSFT", 250.0)

john = Investor("John")
mary = Investor("Mary")

john.add_investment(aapl_stock)
john.add_investment(msft_stock)

mary.add_investment(aapl_stock)

# обновление цену и уведомите инвестор
aapl_stock.update_price(160.0)