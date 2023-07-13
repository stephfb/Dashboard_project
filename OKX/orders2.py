import sys
sys.path.append("../Dashboard_project")  # Add the parent folder to the module search path

import okx.Trade as Trade

def okx_get_open_orders(apikey, secretkey, passphrase, instType="", ordType=""):
    # API initialization
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, "0")

    # Retrieve all incomplete orders
    result = tradeAPI.get_order_list(
        instType=instType,
        ordType=ordType
    )

    # Check for errors
    if result["code"] != "0":
        return None

    # Return the open orders
    return result["data"]
    



if __name__ == "__main__":
    # Your API key, secret key, and passphrase
    okx_api_key= 'e12ebc9b-a94b-4b6b-bf50-146c20ad343d'
    okx_api_secret = '5CC70F28CCFF72CF887E2DCDA59D9ACD'
    okx_passphrase = 'Ops1234!'


    # Retrieve all open orders
    open_orders = okx_get_open_orders(okx_api_key,  okx_api_secret, okx_passphrase)

