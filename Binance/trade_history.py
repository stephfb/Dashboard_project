from binance.client import Client

def get_trade_history(api_key, api_secret):
    client = Client(api_key, api_secret)
    trades = client.futures_account_trades()

    trade_history = []
    for trade in trades:
        symbol = trade['symbol']
        trade_id = trade['id']
        price = float(trade['price'])
        quantity = float(trade['qty'])
        commission = float(trade['commission'])
        time = trade['time']

        trade_history.append({
            'symbol': symbol,
            'trade_id': trade_id,
            'price': price,
            'quantity': quantity,
            'commission': commission,
            'time': time
        })

    return trade_history
