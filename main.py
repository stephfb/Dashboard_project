import config
from orders import get_open_orders
from balance import get_wallet_balance

#binance
api_key= config.api_key
api_secret = config.api_secret

#OKX
#api_key=48a15215-8d3a-4457-a0e2-82f1053d46a4
#api_secret= 9343AECEE7442ABAFBC669905E4B8AF4

# Call functions from other modules, passing the API key and secret
orders = get_open_orders(api_key, api_secret)
balance = get_wallet_balance(api_key, api_secret)

# Print open orders
print("Open Orders:")
for order in orders:
    print(f"Symbol: {order['symbol']}, Type: {order['type']}, Side: {order['side']}, Quantity: {order['quantity']}, Price: {order['price']}")

# Print wallet balance information
print("\nWallet Balance:")
for asset, balance_info in balance.items():
    print(f"Asset: {asset}, Free: {balance_info['free']}, Locked: {balance_info['locked']}")