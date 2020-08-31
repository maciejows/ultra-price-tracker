from pymongo import MongoClient
from scraper.models.Item import Item
from scraper.models.Shop import Shop
from scraper.models.Data import Data
from scraper.webDrvr import *
import datetime


cluster = MongoClient("mongodb+srv://xyz:1234@projektti-5lupj.mongodb.net/scraper?retryWrites=true&w=majority")
db = cluster["scraper"]
ogolna = db["Ogolna"]


data1 = Data(1241324, "01-01-2020")
data2 = Data(7899, "01-03-2020")
data3 = Data(7500, "01-05-2020")
shop1 = Shop("komputronik", "www.komputronik.pl/iphone-7-elo", data1)
shop2 = Shop("morele", "www.morele.pl//apple-iPhone-X-Plus-64GB", data2)
shop3 = Shop("x-kom", "www.x-kom.pl", data3)
item1 = Item("Apple iPhone 7 Plus", shop2)
item2 = Item("Apple iPhone X Plus 64GB", shop3)


def doesUrlExist(url):
    x = ogolna.find_one({"shops.url": url})
    if x is None:
        print("doesn't exist")
        return None
    else:
        print(x)
        return x


def doesNameExist(item_name):
    x = ogolna.find_one({"item_name": item_name})
    if x is None:
        print("doesn't exist")
        return None
    else:
        print(x)
        return x


def addItemToDatabase(item):
    if doesNameExist(item.getName()) is None:
        x = ogolna.find_one(sort=[("_id", -1)])
        if x is None:
            id_ = 0
        else:
            id_ = x["_id"] + 1
        item_frame = {"_id": id_, "item_name": item.getName(), "shops": [{"shop_name": "komputronik", "url": "Null", "data": []},
                                                                      {"shop_name": "morele", "url": "Null", "data": []},
                                                                      {"shop_name": "media-markt", "url": "Null", "data": []},
                                                                      {"shop_name": "media-expert", "url": "Null", "data": []},
                                                                      {"shop_name": "euro", "url": "Null", "data": []},
                                                                      {"shop_name": "x-kom", "url": "Null", "data": []},
                                                                      {"shop_name": "neo24", "url": "Null", "data": []}]}
        ogolna.insert_one(item_frame)
    else:
        return
    # data = {"price": 1999, "date": "01-01-2020"}
    # shop = {"shop_name": "komputronik", "url": "http://", "data": [data]}
    # item = {"_id": ids, "item_name": item_name, "shops": [shop]}


def setShopUrl(item, shop):
    if doesUrlExist(shop.getURL()) is None:
        ogolna.find({"item_name": item.getName()})
        find = {"shops.shop_name": shop.getName()}
        ogolna.update_one(find, {"$set": {"shops.$.url": shop.getURL()}})
    else:
        return
    # ogolna.find({"item_name": item.getName()})
    # find = {"shops.shop_name": shop[0].getName()}



def addDateToShop(item, shop, data):
    ogolna.find = {"item_name": item.getName()}
    find = {"shops.shop_name": shop.getName()}
    x = datetime.datetime.now()
    newData = {"$addToSet": {"shops.$.data": {"price": data.getPrice(), "date": x.strftime("%d-%m-%Y")}}}
    ogolna.update_one(find, newData)


#raczej do wywalenia
def addShopToItem(item, shop):
    find = {"item_name": item.getName()}
    shop = {"shop_name": shop.getName(), "url": shop.getURL()}
    newShop = {"$addToSet": {"shops": shop}}
    ogolna.update_one(find, newShop)


def getShopUrl(item_name, shop_name):
    x = ogolna.find_one({"item_name": item_name})
    for i in x["shops"]:
        y = list(i.values())
        if y[0] == shop_name:
            return y[1]
        else:
            continue


def getShopData(item_name, shop_name):
    x = ogolna.find_one({"item_name": item_name})
    data = []
    for i in x["shops"]:
        y = list(i.values())
        if y[0] == shop_name:
            data.append(y[2])
            break
        else:
            continue
    return data


if __name__ == "__main__":
    # addItemToDatabase(item1)
    # addItemToDatabase(item2)
    # setShopUrl(item1, shop1)
    # setShopUrl(item2, shop2)
    addDateToShop(item1, shop2, data1)
    # addDateToShop(item2, shop2, data3)
    # doesUrlExist("www.x-kom.pl")
    # doesNameExist("Apple iPhone X Plus")
    # print(getShopData("Apple iPhone X Plus", "morele"))
    # print(getShopUrl("Apple iPhone X Plus", "morele"))