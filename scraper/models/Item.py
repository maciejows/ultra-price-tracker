from scraper.models.Shop import Shop


class Item:
    def __init__(self, name):
        self.name = name
        self.shops = self.createEmptyShopArray()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getShops(self):
        return self.shops

    def createEmptyShopArray(self):
        shop_names = ["komputronik", "morele", "media-markt", "media-expert", "euro", "x-kom", "neo24"]
        shop_object = []
        for shop_name in shop_names:
            shop_object.append(Shop(shop_name, None, []))
        return shop_object

    def logItem(self):
        print(self.name)
        for shop in self.shops:
            print(shop.__dict__)

    @property
    def serialize(self):
        shops_serialized = []
        for shop in self.shops:
            shops_serialized.append(shop.serialize)

        return {
            'item_name': self.name,
            'shops': shops_serialized
        }
