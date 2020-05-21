from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# TODO: remove later
class Item:
    def __init__(self, name="Not provided", price=0, thumbnail="Not provided"):
        self.name = name
        self.price = price
        self.thumbnail = thumbnail

    @property
    def serialize(self):
        return {
            'name': self.name,
            'price': self.price,
            'url': self.thumbnail
        }


item = Item("Logitech g920", 1000)


@app.route('/items', methods=["GET"])
def output():
    print("Got request")
    print(request)
    return jsonify(item.serialize)


if __name__ == '__main__':
    app.run("127.0.0.1", "5034")
