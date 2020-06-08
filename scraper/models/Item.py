class Item:

    def __init__(self, name):
        self.name = name
        self.shops = []

    def setName(self, name):
        self.name = name

    def setShop(self, shop, number):
        self.shops[number] = shop

    def addShop(self, shop):
        self.shops.append(shop)

    def getName(self):
        return self.name

    def getShop(self):
        return self.shops
