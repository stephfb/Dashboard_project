import okx.Account as Account

# API initialization
apikey = "48a15215-8d3a-4457-a0e2-82f1053d46a4"
secretkey = "9343AECEE7442ABAFBC669905E4B8AF4"
passphrase = "Hextrust302030!"

flag = "1"  # Production trading:0 , demo trading:1

accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

# Get account balance
result = accountAPI.get_account_balance()
print(result)