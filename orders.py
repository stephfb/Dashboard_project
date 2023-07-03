from binance.client import Client

def get_open_orders(api_key, api_secret):
    client = Client(api_key, api_secret)
    open_orders = client.get_open_orders()

    orders = []
    for order in open_orders:
        symbol = order['symbol']
        order_type = order['type']
        side = order['side']
        quantity = float(order['origQty'])
        price = float(order['price'])

        orders.append({
            'symbol': symbol,
            'type': order_type,
            'side': side,
            'quantity': quantity,
            'price': price
        })

    return orders
