class Item:

    def __init__(self, name, shops):
        self.name = name
        self.shops = [shops]

    def setName(self, name):
        self.name = name

    # def setShop(self, shop, number):
    #     self.shops[number] = shop

    # def addShop(self, shop):
    #     self.shops.append(shop)

    def getName(self):
        return self.name

    def getShops(self):
        return self.shops