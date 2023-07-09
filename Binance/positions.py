from binance.client import Client

def get_position_information(api_key, api_secret):
    client = Client(api_key, api_secret)
    positions = client.futures_position_information()

    position_info = []
    for position in positions:
        position_amount = float(position['positionAmt'])
        if position_amount > 0.0:
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
