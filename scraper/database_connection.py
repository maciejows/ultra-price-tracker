from pymongo import MongoClient
from scraper.models.Item import Item
from scraper.models.Data import Data


cluster = MongoClient("mongodb+srv://xyz:1234@projektti-5lupj.mongodb.net/scraper?retryWrites=true&w=majority")
db = cluster["scraper"]
ogolna = db["Ogolna"]

item1 = Item("Maciej koks2")


def doesNameExist(item_name):
    x = ogolna.find_one({"item_name": item_name})
    if x is None:
        print("doesn't exist")
        return False
    else:
        return True


def addItemToDatabase(item):
    if doesNameExist(item['item_name']) is False:
        x = ogolna.find_one(sort=[("_id", -1)])
        if x is None:
            _id = 0
        else:
            _id = x["_id"] + 1
        item_frame = {"_id": _id, **item}
        ogolna.insert_one(item_frame)
    else:
        print("Item exists")
        return 0


def updateItemInDatabase(item):
    x = ogolna.find_one({"item_name": item['item_name']})
    new_data = {"$set": {"shops": item['shops']}}
    ogolna.update_one(x, new_data)


def getItem(item_name):
    x = ogolna.find_one({"item_name": item_name})
    if x is None:
        return None
    return x


def addDateToShop(item_name, shop_name, data):
    x = ogolna.find_one({"item_name": item_name})
    find = ogolna.find_one({"item_name": item_name, "shops.shop_name": shop_name})
    if x is None or find is None:
        return None
    i = 0
    for shop in find['shops']:
        if shop['shop_name'] == shop_name:
            break
        i += 1

    new_data = {"$push": {f"shops.{i}.data": data.serialize}}
    ogolna.update_one(x, new_data)
    return 1


def getShopUrl(item_name, shop_name):
    x = ogolna.find_one({"item_name": item_name})
    if x is None:
        return None
    for i in x["shops"]:
        if i['shop_name'] == shop_name:
            return i['url']
    return None


def setShopUrl(item_name, shop_name, url):
    x = ogolna.find_one({"item_name": item_name})
    find = ogolna.find_one({"item_name": item_name, "shops.shop_name": shop_name})
    if x is None:
        return None
    i = 0
    for shop in find['shops']:
        if shop['shop_name'] == shop_name:
            break
        i += 1

    new_data = {"$set": {f"shops.{i}.url": url}}
    ogolna.update_one(x, new_data)
    return 1


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


def doesUrlExist(url):
    x = ogolna.find_one({"shops.url": url})
    if x is None:
        print("doesn't exist")
        return None
    else:
        print(x)
        return x
