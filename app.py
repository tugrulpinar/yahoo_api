import requests
import os

# Hide your API KEY
KEY = os.environ["YAHOO_KEY"]

# KEY = "Uuu04gRjLsanSr1b9JUXp3PzTXY7kMjV8mIFlMq3"


class YahooApi:
    def __init__(self):
        self.url = "https://rest.yahoofinanceapi.com/v6/finance/quote"

    def get_last_close_price(self, symbol: str) -> int:
        """Gets the latest closing price"""

        querystring = {"symbols": symbol}

        headers = {
            'x-api-key': KEY
        }

        try:
            response = requests.get(
                self.url, headers=headers, params=querystring)

            res = response.json()

            return res["quoteResponse"]["result"][0]["regularMarketPreviousClose"]

        except Exception as e:
            return e


yahoo = YahooApi()
print(yahoo.get_last_close_price("MSFT"))
