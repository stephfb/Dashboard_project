import sys
sys.path.append("../Dashboard_project")  # Add the parent folder to the module search path

import config  # Import the config module from the parent folder

import okx.Account as Account

def create_okx_positions_dictionary(positions_data):
    positions_dict = []
    if isinstance(positions_data, list):
        for position in positions_data:
            position_dict = {
                'Symbol':position['instId'],
                'Size': position['pos'],
                'Entry Price': position['avgPx'],
                'Margin': position['margin'],
                'Mark Price': position['markPx'],
                'Margin Level': position['mgnRatio'],
                'Est Liquidity Price': position['liqPx'],
                'PnL': position['upl'],
                'PnL%': position['uplRatio']
            }
            positions_dict.append(position_dict)
    return positions_dict

def okx_get_positions(apikey, secretkey, passphrase):
    apikey = config.okx_api_key
    secretkey = config.okx_api_secret
    passphrase = config.okx_passphrase

    flag = "0"  # Production trading: 0, Demo trading: 1

    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

    # Get positions information
    result = accountAPI.get_positions()

    positions_data = result['data'] if 'data' in result else []

    # Convert positions data to dictionary
    positions_dict = create_okx_positions_dictionary(positions_data)

    return positions_dict
