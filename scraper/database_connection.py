from pymongo import MongoClient
from scraper.models.Item import Item
from scraper.models.Shop import Shop
from scraper.models.Data import Data
from scraper.webDrvr import *


cluster = MongoClient("mongodb+srv://xyz:1234@projektti-5lupj.mongodb.net/scraper?retryWrites=true&w=majority")
db = cluster["scraper"]
ogolna = db["Ogolna"]
data1 = Data(7999, "01-01-2020")
data2 = Data(7899, "01-03-2020")
data3 = Data(7500, "01-05-2020")
shop1 = Shop("komputronik", "www.komputronik.pl", data1)
shop2 = Shop("morele", "www.morele.pl", data2)
shop3 = Shop("x-kom", "www.x-kom.pl", data3)
item1 = Item("Apple iPhone 7", shop1)


def addItemToDatabase(item):
    ids = 1

    itemzzz = {"_id": ids, "item_name": item.getName(), "shops": [{"shop_name": "komputronik", "url": "Null", "data": "Null"},
                                                                  {"shop_name": "morele", "url": "Null", "data": "Null"},
                                                                  {"shop_name": "media-markt", "url": "Null", "data": "Null"},
                                                                  {"shop_name": "media-expert", "url": "Null", "data": "Null"},
                                                                  {"shop_name": "euro", "url": "Null", "data": "Null"},
                                                                  {"shop_name": "x-kom", "url": "Null", "data": "Null"},
                                                                  {"shop_name": "neo24", "url": "Null", "data": "Null"}]}

    ogolna.find({"_id": 1})
    find = {"shops.$.shop_name": "komputronik"}
    ogolna.replace_one(find, {"$set": {"shops.url": "http://"}})
    # data = {"price": 1999, "date": "01-01-2020"}
    # shop = {"shop_name": "komputronik", "url": "http://", "data": [data]}
    # item = {"_id": ids, "item_name": item_name, "shops": [shop]}
    # ogolna.insert_one(itemzzz)


def addShopToItem(item, shop):
    find = {"item_name": item.getName()}
    # data = {"price": 2349, "date": "02-01-2020"}
    shop = {"shop_name": shop.getName(), "url": shop.getURL()}
    newShop = {"$addToSet": {"shops": shop}}
    ogolna.update_one(find, newShop)


def addDateToShop(item_name, shop_name, data):
    ogolna.find = {"item_name": item_name}
    find = {"shops.shop_name": shop_name}
    newData = {"$addToSet": {"shops.$.data": {"price": data.getPrice(), "date": data.getDate()}}}
    ogolna.update_one(find, newData)

if __name__ == "__main__":
    # addToDatabase()
    # addItemToDatabase("Logitech g920555")
    # addShopToItem("Logitech g920555", "morele", "httttttp://///")
    # addDateToShop("Logitech g920", "morele", data3)
    addItemToDatabase(item1)