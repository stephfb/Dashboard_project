import requests
import json
import os

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")


def get_open_perpetual_positions():
    # API endpoint for account information
    url = "https://fapi.binance.com/fapi/v2/account"

    # Generate timestamp
    timestamp = int(time.time() * 1000)

    # Generate signature
    query_string = f"timestamp={timestamp}"
    signature = hmac.new(api_secret.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()

    # Prepare headers
    headers = {
        "X-MBX-APIKEY": api_key
    }

    # Send GET request
    response = requests.get(url, headers=headers, params={"timestamp": timestamp, "signature": signature})

    # Check response status
    if response.status_code == 200:
        account_info = json.loads(response.text)

        # Extract open positions
        open_positions = []
        for position in account_info['positions']:
            if float(position['positionAmt']) != 0:
                open_positions.append(position)

        return open_positions
    else:
        print(f"Error retrieving account information: {response.status_code} - {response.text}")
        return None