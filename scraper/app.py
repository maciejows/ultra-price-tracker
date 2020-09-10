from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
import scraper.database_connection as db
import scraper.driver_interface as wdi
from scraper.models.Data import Data
from scraper.models.Item import Item

app = Flask(__name__)
CORS(app)


@app.route('/items', methods=["GET"])
def output():
    args = request.args
    # Check if name in query params
    if "name" in args:
        item = db.getItem(args['name'])
        if item is not None:
            # Check urls
            if isUrlMissing(item):
                data = wdi.get_all_data_phrase(args['name'])
                item = fillData(item, data)
            else:
                data = {}
                for shop in item['shops']:
                    wdi_result = wdi.get_data_from_url(shop['url'])
                    data[shop['shop_name']] = wdi_result
                item = fillData(item, data)
            # Update Db
            db.updateItemInDatabase(item)
        else:
            item = Item(args['name'])
            data = wdi.get_all_data_phrase(args['name'])
            item = fillData(item.serialize, data)
            # Add to Db
            db.addItemToDatabase(item)
        return jsonify(item)
    else:
        return make_response("Bad request", 400)


def isUrlMissing(item):
    for shop in item['shops']:
        # Url is missing
        if shop['url'] is None:
            return True
    return False


def fillData(item, data):
    i = 0
    values = list(data.values())
    for shop in item['shops']:
        shop['url'] = values[i]['link']
        shop['data'].append(Data(values[i]['price']).serialize)
        i += 1
    return item


if __name__ == '__main__':
    print("Przed")
    #print(wdi.get_all_data_phrase("apple iphone 7"))
    #print(wdi.get_all_data_url("https://www.morele.net/smartfon-apple-iphone-7-32-gb-czarny-mn8x2pm-a-1021730/"))
    #print(wdi.get_missing_data("Apple iPhone 7")) #wywala session-id
    #print(wdi.get_data_from_url("https://www.morele.net/smartfon-apple-iphone-7-32-gb-czarny-mn8x2pm-a-1021730/"))
    print("Po")
    app.run("127.0.0.1", "4100")

    #print(wdi.get_new_prices())
    #wdi.get_data_from_url()