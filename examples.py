import requests
import os
from config import base_url,api_key,secret_key
import stock_algo as tradeapi
url = f'{base_url}/v2/account'
headers= {'APCA-API-KEY-ID':api_key,'APCA-API-SECRET-KEY':secret_key}
r = requests.get(url,headers=headers)
print(r.text)

api = tradeapi.REST(api_key,secret_key,base_url)
account = api.get_account()
print(account)