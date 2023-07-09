import okex.v5.account_api as account_api
import config

def get_wallet_balance():
    client = account_api.AccountAPI(config.api_key, config.api_secret, config.passphrase, False)
    # Implement the logic to retrieve the wallet balance from OKEX API
    # Return the balance data in a suitable format
    return balance_data