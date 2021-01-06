import requests
import os
from config import base_url,api_key,secret_key
url = f'{base_url}/v2/account'
headers= {'APCA-API-KEY-ID':api_key,'APCA-API-SECRET-KEY':secret_key}
r = requests.get(url,headers=headers)
print(r.text)