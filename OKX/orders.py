import sys
sys.path.append("../Dashboard_project")  # Add the parent folder to the module search path

import config  # Import the config module from the parent folder

import okx.Trade as Trade

def create_okx_orders_dictionary(orders_data):
    orders_dict = {}
    if isinstance(orders_data, list):
        for order in orders_data:
            order_id = order['ordId']
            orders_dict[order_id] = {
                'Symbol': order['instId'],
                'Order Time': order['cTime'],
                'Type': order['instType'],
                'Side': order['side'],
                'Order Type': order['ordType'],
                'Fill Price': order['fillPx'],
                'Fill Size': order['fillSz'],
                'Fill Time': order['fillTime'],
                'State': order['state']
            }
    return orders_dict

def get_order_list(okx_api_key, okx_api_secret, okx_passphrase): 
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

    # Convert orders data to dictionary
    orders_dict = create_okx_orders_dictionary(result)

    return orders_dict


