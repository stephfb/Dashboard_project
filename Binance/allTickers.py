from binance.client import Client
import sys
sys.path.append("../Dashboard_project-main")  # Add the parent folder to the module search path
import config  # Import the config module from the parent folder
import requests
import json

api_url = "https://api.binance.com/api/v3/ticker/price"


#Make a GET request to the API endpoint
response = requests.get(api_url)

data = json.loads(response.content)


# binance_api_key = config.BINANCE_KEY
# binance_api_secret = config.BINANCE_SECRET

# client = Client(binance_api_key, binance_api_secret)
# trades = client.()

binance_tickers = []
for pair in data:
    binance_tickers.append(pair['symbol'])
#print(binance_tickers)


