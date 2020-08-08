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
item1 = Item("Apple iPhone 7", shop2)
item2 = Item("Apple iPhone X", shop3)


def addItemToDatabase(item):

    item_frame = {"_id": Item.id, "item_name": item.getName(), "shops": [{"shop_name": "komputronik", "url": "Null", "data": []},
                                                                  {"shop_name": "morele", "url": "Null", "data": []},
                                                                  {"shop_name": "media-markt", "url": "Null", "data": []},
                                                                  {"shop_name": "media-expert", "url": "Null", "data": []},
                                                                  {"shop_name": "euro", "url": "Null", "data": []},
                                                                  {"shop_name": "x-kom", "url": "Null", "data": []},
                                                                  {"shop_name": "neo24", "url": "Null", "data": []}]}

    Item.id += 1
    ogolna.insert_one(item_frame)
    # data = {"price": 1999, "date": "01-01-2020"}
    # shop = {"shop_name": "komputronik", "url": "http://", "data": [data]}
    # item = {"_id": ids, "item_name": item_name, "shops": [shop]}


def setShopUrl(item, shop):

    # ogolna.find({"item_name": item.getName()})
    # find = {"shops.shop_name": shop[0].getName()}

    ogolna.find({"item_name": item.getName()})
    find = {"shops.shop_name": shop.getName()}
    ogolna.update_one(find, {"$set": {"shops.$.url": shop.getURL()}})


def addDateToShop(item, shop, data):
    ogolna.find = {"item_name": item.getName()}
    find = {"shops.shop_name": shop.getName()}
    newData = {"$addToSet": {"shops.$.data": {"price": data.getPrice(), "date": data.getDate()}}}
    ogolna.update_one(find, newData)


def addShopToItem(item, shop):
    find = {"item_name": item.getName()}
    shop = {"shop_name": shop.getName(), "url": shop.getURL()}
    newShop = {"$addToSet": {"shops": shop}}
    ogolna.update_one(find, newShop)


if __name__ == "__main__":
    addItemToDatabase(item1)
    addItemToDatabase(item2)
    setShopUrl(item1, shop2)
    addDateToShop(item1, shop2, data3)