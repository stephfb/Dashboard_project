import sys
sys.path.append("../Dashboard_project")  # Add the parent folder to the module search path
import config  # Import the config module from the parent folder

import okx.Account as Account

def okx_get_positions(apikey, secretkey, passphrase):
    apikey = config.okx_api_key
    secretkey = config.okx_api_secret
    passphrase = config.okx_passphrase

    flag = "0"  # Production trading: 0, Demo trading: 1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

# Get positions information
    result = accountAPI.get_positions()

    return result
