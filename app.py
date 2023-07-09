import config
from flask import Flask, render_template
from Binance.orders import get_open_orders
from Binance.positions import get_position_information
from Binance.balance import get_wallet_balance
from Binance.trade_history import get_trade_history


app = Flask(__name__)

@app.route('/')
def dashboard():
    api_key = config.api_key
    api_secret = config.api_secret

    # Retrieve data from modules
    orders = get_open_orders(api_key, api_secret)
    balance = get_wallet_balance(api_key, api_secret)
    positions = get_position_information(api_key, api_secret)
    trades = get_trade_history(api_key, api_secret)

    return render_template('dashboard.html', orders=orders, positions=positions, balance=balance, trades=trades)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
