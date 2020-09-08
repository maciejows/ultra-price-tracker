from pymongo import MongoClient
from scraper.models.Item import Item
from scraper.models.Shop import Shop
from scraper.models.Data import Data


cluster = MongoClient("mongodb+srv://xyz:1234@projektti-5lupj.mongodb.net/scraper?retryWrites=true&w=majority")
db = cluster["scraper"]
ogolna = db["Ogolna"]

item1 = Item("Maciej koks2")
item2 = Item("Apple iPhone X Plus 64GB")

item1.logItem()


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
        item_frame = {"_id": id_, **item.serialize}
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
    newData = {"$addToSet": {"shops.$.data": Data()}}
    ogolna.update_one(find, newData)


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
      addItemToDatabase(item1)
    # addItemToDatabase(item2)
    # setShopUrl(item1, shop1)
    # setShopUrl(item2, shop2)
    # addDateToShop(item1, shop2, data1)
    # addDateToShop(item2, shop2, data3)
    # doesUrlExist("www.x-kom.pl")
    # doesNameExist("Apple iPhone X Plus")
    # print(getShopData("Apple iPhone X Plus", "morele"))
    # print(getShopUrl("Apple iPhone X Plus", "morele"))
