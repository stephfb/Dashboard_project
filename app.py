import config
from flask import Flask, render_template
from orders import get_open_orders
from balance import get_wallet_balance

app = Flask(__name__)

@app.route('/')
def dashboard():
    api_key = config.api_key
    api_secret = config.api_secret

    # Retrieve data from modules
    orders = get_open_orders(api_key, api_secret)
    balance = get_wallet_balance(api_key, api_secret)

    return render_template('dashboard.html', orders=orders, balance=balance)


if __name__ == '__main__':
    app.run(debug=True)

