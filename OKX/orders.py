import sys
sys.path.append("../Dashboard_project")  # Add the parent folder to the module search path

import config  # Import the config module from the parent folder

import okx.Trade as Trade

def create_okx_orders_dictionary(orders_data):
    orders_dict =[]
    if isinstance(orders_data, list):
        for order in orders_data:
            orders_dict.append({
                'Symbol': order['instId'],
                'Time': order['uTime'],
                'Side': order['side'],
                'Filled': order['fillSz'],
                'Filled Price': order['fillPx'],
            })
    else:
        orders_dict = {}
    return orders_dict

#Connect to API
def okx_get_order_list(apikey, secretkey, passphrase): 
    apikey = config.okx_api_key
    secretkey = config.okx_api_secret
    passphrase = config.okx_passphrase
    
    flag = "0"  # Production trading: 0, Demo trading: 1

    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

    #Get orders information 

    result = tradeAPI.get_order_list(instType="",
        ordType="")

    orders_data = result['data'] if 'data' in result else []

    #Convert orders data to dictionary 

    orders_dict = create_okx_orders_dictionary(orders_data)

    return orders_dict
    #print(orders_dict)
