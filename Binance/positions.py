from binance.client import Client
import sys
sys.path.append("../Dashboard_project-main")  # Add the parent folder to the module search path
import config

def binance_get_positions(api_key, api_secret):
    client = Client(api_key, api_secret)
    positions = client.futures_position_information()

    position_info = []
    for position in positions:
        position_amount = float(position['positionAmt'])
        #if position_amount > 0.0:
        symbol = position['symbol']
        entry_price = float(position['entryPrice'])
        mark_price = float(position['markPrice'])
        unrealized_profit = float(position['unRealizedProfit'])

        position_info.append({
            'symbol': symbol,
            'amount': position_amount,
            'entry_price': entry_price,
            'mark_price': mark_price,
            'unrealized_profit': unrealized_profit
        })

    return position_info

if __name__ == "__main__":
    # Your API key, secret key, and passphrase
    binance_api_key = config.BINANCE_KEY
    binance_api_secret = config.BINANCE_SECRET


    # Retrieve all open orders
    #open_orders = okx_get_open_orders(okx_api_key,  okx_api_secret, okx_passphrase)
    binance_positions = binance_get_positions(binance_api_key, binance_api_secret)
    for pos in binance_positions:
        print(pos['symbol'])
   
