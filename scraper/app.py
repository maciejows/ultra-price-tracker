from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/item', methods=["GET"])
def output():
    print("Got request")
    print(request)
    return jsonify("XD")


if __name__ == '__main__':
    app.run("127.0.0.1","5034")