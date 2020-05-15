from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://xyz:1234@projektti-5lupj.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["scraper"]
ogolna = db["0golna"]
euro = db["euro"]
komputronik = db["komputronik"]
mediaexpert = db["mediaexpert"]
mediamarkt = db["mediamarkt"]
morele = db["morele"]
neonet = db["neonet"]
test = db["test"]

post = {"_id": 1, "model": "TCL 50Eqw40", "cena": 1566, "URL": "https://www.euro.com.pl/telewizory-led-lcd-plazmowe/tcl-5234640-tv-led-4k-android.bhtml"}

komputronik.insert_one(post)

