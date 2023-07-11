import sys
sys.path.append("../Dashboard_project")  # Add the parent folder to the module search path
import config  # Import the config module from the parent folder

import okx.Account as Account

def create_okx_balance_dictionary(balance_data):
    balance_dict = {}
    if isinstance(balance_data, list):
        for balance in balance_data:
            details = balance.get('details', [])
            for detail in details:
                asset = detail.get('ccy', '')
                equity = detail.get('eq', '')
                cash_balance = detail.get('cashBal', '')
                isolated_margin_equity = detail.get('isoEq', '')
                available_equity = detail.get('availEq', '')
                balance_dict[asset] = {
                    'Equity': equity,
                    'Cash Balance': cash_balance,
                    'Isolated Margin Equity': isolated_margin_equity,
                    'Available Equity': available_equity
                }
    return balance_dict

def okx_get_account_balance(apikey, secretkey, passphrase):
    apikey = config.okx_api_key
    secretkey = config.okx_api_secret
    passphrase = config.okx_passphrase
    
    flag = "0"  # Production trading: 0, Demo trading: 1

    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

    # Get account balance
    result = accountAPI.get_account_balance()

    balance_data = result['data'] if 'data' in result else []

    # Convert balance data to dictionary
    balance_dict = create_okx_balance_dictionary(balance_data)

    return balance_dict
