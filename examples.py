import requests
import os
import stock_algo as tradeapi
import requests
from config import base_url,api_key,secret_key
# url = f'{base_url}/v2/account'
# headers= {'APCA-API-KEY-ID':api_key,'APCA-API-SECRET-KEY':secret_key}
# s = requests.Session()
# r = s.request(method='GET',url=url,headers=headers)
# print(r)
# print(r.text)

api = tradeapi.REST(api_key = api_key,
                    secret_key = secret_key,
                    base_url  =base_url)
# print(api.__str__())
account = api.get_account()
print(account.status)