from pymongo import MongoClient
from scraper.models.Item import Item
from scraper.models.Shop import Shop
from scraper.models.Data import Data
from scraper.webDrvr import *

cluster = MongoClient("mongodb+srv://xyz:1234@projektti-5lupj.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["scraper"]
ogolna = db["Ogolna"]

def addItemToDatabase(item_name):
    ids = 0
    data = {"price": 1999, "date": "01-01-2020"}
    shop = {"shop_name": "komputronik", "url": "http://", "data": [data]}
    item = {"_id": ids, "item_name": item_name, "shop": [shop]}
    ogolna.insert_one(item)


def addShopToItem(item_name):
    find = {"item_name": item_name}
    data = {"price": 2349, "date": "02-01-2020"}
    shop = {"shop_name": "morele", "url": "http://", "data": [data]}
    newShop = {"$addToSet": {"shop": shop}}
    ogolna.update_one(find, newShop)


def addDateToShop(item_name):
    find = {"item_name": item_name}
    data = {"price": 2500, "date": "05-09-2020"}
    newShop = {"$push": {"shop.$.data": data}}
    ogolna.update_one(find, newShop)


if __name__ == "__main__":
    # addToDatabase()
    # addItemToDatabase("Logitech g920")
    addShopToItem("Logitech g920")
    # addDateToShop("Logitech g920")
