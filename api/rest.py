import logging
import os
from requests.exceptions import HTTPError
import time
from config import base_url,api_key,secret_key


logger = logging.getLogger(__name__)

class RetryException(Exception):
    pass
class APIError(Exception):
    def __init__(self,
                error,
                http_error=None):
        super().__init__(error['message'])
        self._error = error
        self._http_error = http_error
    
    @property
    def code(self):
        return self._error['code']
    
    @property 
    def status_code(self):
        http_error = self._http_error
        if http_error is not None and hasattr(http_error,'response'):
            return http_error.reponse.status_code
    
    @property
    def request(self):
        if self._http_error is not None:
            return self._http_error.request
    
    @property
    def response(self):
        if self._http_error is not None:
            return self._http_error.response
    

class REST(object):
    def __init__(self,
                api_key:str=api_key,
                secret_key:str=secret_key,
                base_url:str=base_url,
                api_version:str='v2'
                ):
        self._api_key = api_key
        self._secret_key = secret_key
        self._base_url  = base_url
        self._api_version = api_version
        self._session = requests.Session()
        self._retry = int(os.environ.get('APCA_RETRY_MAX', 3))
        self._retry_wait = int(os.environ.get('APCA_RETRY_WAIT', 3))
        self._retry_codes = [int(o) for o in os.environ.get(
            'APCA_RETRY_CODES', '429,504').split(',')]

    def _request(self,
                method,
                path,
                data=None,
                base_url:str=base_url,
                api_version:str='v2'):
        base_url = base_url or self._base_url
        url:str = f'{base_url}/{version}/{path}'
        headers:dict= {'APCA-API-KEY-ID':self._api_key,'APCA-API-SECRET-KEY':self._secret_key}
        retry = self._retry

         
    