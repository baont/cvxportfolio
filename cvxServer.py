from flask import Flask
from tinydb import TinyDB, Query
import sqlite3
import dataset

supportCoins = ["BTC",
                "ETH",
                "LTC",
                "NEO",
                "XRP",
                "BNB",
                "BGBP",
                "EOS",
                "TRX",
                "LINK",
                "ALGO",
                "WIN",
                "BCH",
                "BTT",
                "ADA",
                "ZEC",
                "ATOM",
                "DUSK",
                "ONE",
                "XLM",
                "BAT",
                "FTM",
                "PERL",
                "ONT",
                "TOMO",
                "USDS",
                "WAVES"]

app = Flask(__name__)

@app.route('/getAdvice')
def createAdvice():
    # fist must pull the most recent tick of the market
    return "Hello World!"

if __name__ == '__main__':
    app.run()