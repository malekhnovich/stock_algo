import requests
import os
base_url  = os.getenv('APCA_API_BASE_URL')
api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')
url = f'{base_url}/v2/account'
headers= {'APCA-API-KEY-ID':api_key,'APCA-API-SECRET-KEY':secret_key}
r = requests.get(url,headers=headers)
print(r.text)