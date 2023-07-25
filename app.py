import config
import sys
sys.path.append("../Dashboard_project-main")
from flask import Flask, render_template, jsonify
from Binance.orders import get_open_orders
from Binance.positions import binance_get_positions
from Binance.balance import get_wallet_balance
from Binance.trade_history import get_trade_history
from OKX.balance import okx_get_account_balance
from OKX.orders import okx_get_order_list
from OKX.positions import okx_get_positions
from Binance.allTickers import *
import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():
    try:
        # Retrieve Binance data
        binance_api_key = config.BINANCE_KEY
        binance_api_secret = config.BINANCE_SECRET
        binance_orders = get_open_orders(binance_api_key, binance_api_secret)
        binance_positions = binance_get_positions(binance_api_key, binance_api_secret)
        binance_balance = get_wallet_balance(binance_api_key, binance_api_secret)


        binance_trades = {}
        now = datetime.datetime.utcnow()

        # Calculate the number of seconds in a week
        one_week = datetime.timedelta(weeks=1).total_seconds()

        # Subtract one week from the current time to get the time one week ago
        one_week_ago = now - datetime.timedelta(seconds=one_week)
        start_time = int(one_week_ago.timestamp())
        for symbol in binance_tickers:
            binance_trades[symbol] = get_trade_history(binance_api_key, binance_api_secret, symbol, start_time)
    except Exception as e:
        # Handle Binance API connection error
        binance_orders = []
        binance_positions = []
        binance_balance = {}
        binance_trades = []
        print(f"Error connecting to Binance API: {str(e)}")

    try:
        # Retrieve OKX data
        okx_api_key = config.okx_api_key
        okx_api_secret = config.okx_api_secret
        okx_passphrase = config.okx_passphrase
        okx_balance = okx_get_account_balance(okx_api_key, okx_api_secret, okx_passphrase)
        okx_orders = okx_get_order_list(okx_api_key, okx_api_secret, okx_passphrase)
        okx_positions = okx_get_positions(okx_api_key, okx_api_secret, okx_passphrase)
    except Exception as e:
        # Handle OKX API connection error
        okx_balance = []
        okx_orders = []
        okx_positions = []
        print(f"Error connecting to OKX API: {str(e)}")

    try:
        
        ticker_dict = {}

        for transaction in binance_trades:
            ticker = transaction["symbol"]
            if ticker not in ticker_dict:
                ticker_dict[ticker] = []
            ticker_dict[ticker].append(transaction)
    except Exception as e:
        ticker_dict = {}

    return render_template('dashboard.html',
                           binance_orders=binance_orders,
                           binance_balance=binance_balance,
                           binance_positions=binance_positions,
                           binance_trades=binance_trades,
                           okx_balance=okx_balance,
                           okx_orders=okx_orders,
                           okx_positions=okx_positions,
                           okx_length=len(okx_balance),
                           binance_length=len(binance_balance),
                           tickers=list(ticker_dict.keys()))

@app.route('/transactions/<ticker>')
def get_transactions(ticker):
    ticker_dict = binance_tickers
    if ticker in ticker_dict:
        return jsonify(ticker_dict[ticker])
    else:
        return jsonify([])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    

