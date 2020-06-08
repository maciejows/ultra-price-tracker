class Data:

    def __init__(self, price, date):
        self.price = price
        self.date = date

    def setPrice(self, price):
        self.price = price

    def setDate(self, date):
        self.date = date

    def getPrice(self):
        return self.price

    def getDate(self):
        return self.date
