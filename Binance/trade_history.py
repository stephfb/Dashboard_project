import requests
import json
import hashlib
import hmac
import time
from urllib.parse import urlencode
import config

def get_trade_history(api_key, api_secret):
    endpoint = "/fapi/v1/userTrades"
    method = "GET"
    timestamp = int(time.time() * 1000)
    params = {
        "symbol": "BTCUSDT",  # Update with your desired symbol
        "timestamp": timestamp
    }
    query_string = urlencode(params)
    signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    headers = {
        "X-MBX-APIKEY": api_key
    }

    url = f"https://fapi.binance.com{endpoint}?{query_string}&signature={signature}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        trades = json.loads(response.text)
        return trades
    else:
        print(f"Error: {response.text}")
        return []

