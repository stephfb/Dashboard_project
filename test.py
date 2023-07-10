
import sys
sys.path.append("../Dashboard_project")  # Add the parent folder to the module search path
import config  # Import the config module from the parent folder
from okx.Account import AccountAPI

def get_account_balance():
    apikey = config.okx_api_key
    secretkey = config.okx_api_secret
    passphrase = config.okx_passphrase
    
    flag = "0"  # Production trading:0 , demo trading:1

    accountAPI = AccountAPI(apikey, secretkey, passphrase, False, flag)

    # Get account balance
    result = accountAPI.get_account_balance()
    
    return result

# Test the module
balance = get_account_balance()
print(balance)
#test

