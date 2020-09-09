import datetime

class Data:
    def __init__(self, price):
        self.price = price
        self.date = datetime.datetime.now().strftime("%d-%m-%Y")

    def setPrice(self, price):
        self.price = price

    def setDate(self, date):
        self.date = date

    def getPrice(self):
        return self.price

    def getDate(self):
        return self.date

    @property
    def serialize(self):
        return {
            "price": self.price,
            "date": self.date
        }
