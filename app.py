import config
from flask import Flask, render_template
from Binance.orders import get_open_orders
from Binance.positions import binance_get_positions
from Binance.balance import get_wallet_balance
from Binance.trade_history import get_trade_history
from OKX.balance import get_account_balance
from OKX.orders import get_order_list
from OKX.positions import okx_get_positions

app = Flask(__name__)


@app.route('/')
def dashboard():
    # Retrieve Binance data
    binance_api_key = config.binance_api_key
    binance_api_secret = config.binance_api_secret
    binance_orders = get_open_orders(binance_api_key, binance_api_secret)
    binance_positions = binance_get_positions(binance_api_key, binance_api_secret)
    binance_balance = get_wallet_balance(binance_api_key, binance_api_secret)
    binance_trades = get_trade_history(binance_api_key, binance_api_secret)

    #Retrieve OKX data
    okx_api_key = config.okx_api_key
    okx_api_secret = config.okx_api_secret
    okx_passphrase = config.okx_passphrase
    okx_balance = get_account_balance(okx_api_key, okx_api_secret, okx_passphrase)
    okx_orders = get_order_list(okx_api_key, okx_api_secret, okx_passphrase)
    okx_positions = okx_get_positions(okx_api_key, okx_api_secret, okx_passphrase)

    return render_template('dashboard.html',
                           binance_orders=binance_orders,
                           binance_balance=binance_balance,
                           binance_positions=binance_positions,
                           binance_trades=binance_trades,
                           okx_balance=okx_balance,
                           okx_orders=okx_orders,
                           okx_positions=okx_positions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
