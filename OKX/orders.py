import sys
sys.path.append("../Dashboard_project")  # Add the parent folder to the module search path

import config  # Import the config module from the parent folder
import okx.Trade as Trade

def get_order_list(apikey, secretkey, passphrase): 
    apikey = config.okx_api_key
    secretkey = config.okx_api_secret
    passphrase = config.okx_passphrase
    
    flag = "0"  # Production trading: 0, Demo trading: 1

    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

    # Retrieve all incomplete orders
    
    result = tradeAPI.get_order_list(
        instType="SPOT",
        ordType="post_only,fok,ioc"
    )

    return result

