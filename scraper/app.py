from flask import Flask, jsonify, make_response
from flask_cors import CORS
import scraper.database_connection as db

app = Flask(__name__)
CORS(app)


@app.route('/items', methods=["GET"])
def output():
    item = db.getItem("Apple iPhone 7")
    if item is not None:
        return jsonify(item)
    else:
        return make_response("Record not found", 400)


if __name__ == '__main__':
    app.run("127.0.0.1", "5034")
