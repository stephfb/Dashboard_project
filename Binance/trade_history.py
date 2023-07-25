from binance.client import Client
import datetime
import sys
sys.path.append("../Dashboard_project-main")  # Add the parent folder to the module search path
import config
from Binance.allTickers import *

def get_trade_history(api_key, api_secret, symbol, startTime):
    client = Client(api_key, api_secret)
    trades = client.get_my_trades(symbol=symbol, startTime = startTime)

    trade_history = []
    # for trade in trades:
    #     symbol = trade['symbol']
    #     trade_id = trade['id']
    #     price = float(trade['price'])
    #     quantity = float(trade['qty'])
    #     commission = float(trade['commission'])
    #     time = trade['time']

    #     trade_history.append({
    #         'symbol': symbol,
    #         'trade_id': trade_id,
    #         'price': price,
    #         'quantity': quantity,
    #         'commission': commission,
    #         'time': time
    #     })

    for trade in trades:
        #symbol = trade['symbol']
        trade_id = trade['id']
        #order_list_id = trade['"orderListId"'] #Unless OCO, the value will always be -1
        order_id = trade['orderId']
        price = float(trade['price'])
        quantity = float(trade["qty"])
        quote_quantity = float(trade["quoteQty"])
        commission = float(trade['commission'])
        commission_asset = trade["commissionAsset"]
        time = trade['time']

        trade_history.append({
            "symbol": symbol,
            "id": trade_id,
            "orderId": order_id,
            #"orderListId": order_list_id, #Unless OCO, the value will always be -1
            "price": price,
            "qty": quantity,
            "quoteQty": quote_quantity,
            "commission": commission,
            "commissionAsset": commission_asset,
            "time": time,
        })

    return trade_history

if __name__ == "__main__":
    # Your API key, secret key, and passphrase
    binance_api_key = config.BINANCE_KEY
    binance_api_secret = config.BINANCE_SECRET

    # Retrieve all open orders
    #open_orders = okx_get_open_orders(okx_api_key,  okx_api_secret, okx_passphrase)
    trades = []

    # Get the current time in UTC
    now = datetime.datetime.utcnow()

    # Calculate the number of seconds in a week
    one_week = datetime.timedelta(weeks=1).total_seconds()

    # Subtract one week from the current time to get the time one week ago
    one_week_ago = now - datetime.timedelta(seconds=one_week)

    tickers = binance_tickers
    
    trades = get_trade_history(binance_api_key, binance_api_secret,"ATOMUSDT",int(one_week_ago.timestamp()))
    print(trades)

