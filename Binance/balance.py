from binance.client import Client

def get_wallet_balance(api_key, api_secret):
    client = Client(api_key, api_secret)
    account_info = client.get_account()

    balances = {}
    for balance in account_info['balances']:
        if float(balance['free']) > 0.0 or float(balance['locked']) > 0.0:
            asset = balance['asset']
            free_balance = float(balance['free'])
            locked_balance = float(balance['locked'])
            balances[asset] = {
                'free': free_balance,
                'locked': locked_balance
            }

    return balances
