from binance.client import Client
from datetime import datetime

def get_open_orders(api_key, api_secret):
    client = Client(api_key, api_secret)
    open_orders = client.get_open_orders()

    orders = []
    for order in open_orders:
        symbol = order['symbol']
        timestamp = int(order['time']) / 1000  # Convert from milliseconds to seconds
        time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')  # Convert to readable format
        order_type = order['type']
        side = order['side']
        icebergqty = order['icebergQty']
        filled = order['executedQty']
        quantity = float(order['origQty'])
        price = float(order['price'])

        orders.append({
            'symbol': symbol,
            'type': order_type,
            'side': side,
            'quantity': quantity,
            'price': price,
            'executedqty': filled,
            'icebergqty': icebergqty,
            'time': time
        })

    return orders
