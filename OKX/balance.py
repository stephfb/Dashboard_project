import okx.Account as Account


# API initialization
apikey = "cf4f49a4-487a-402c-a878-09a8cb012aa6"
secretkey = "3F249530E953B3AF77666C20B5A327D5"
passphrase = "Hextrust302030!"

flag = "0"  # Production trading:0 , demo trading:1

accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

# Get account balance
result = accountAPI.get_account_balance()
print(result)

