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

    # Return the open orders

    print(result)



apikey= 'e12ebc9b-a94b-4b6b-bf50-146c20ad343d'
secretkey = '5CC70F28CCFF72CF887E2DCDA59D9ACD'
passphrase = 'Ops1234!'

okx_get_open_orders(apikey, secretkey, passphrase,instType="SPOT",
    ordType="post_only,fok,ioc")
    
