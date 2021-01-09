import logging
import os
import requests
from requests.exceptions import HTTPError
import time
from .entity import Account,Orders


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
                api_key:str,
                secret_key:str,
                base_url:str,
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
    def __str__(self):
        return f'API_KEY is {self._api_key} and SECRET_KEY is {self._secret_key}'
    def __repr__(self):
        return f'REST(API_KEY={self._api_key},SECRET_KEY={self._secret_key},BASE_URL={self._base_url})'
    

    def _request(self,
                method,
                path,
                base_url:str,
                data=None,
                api_version:str='v2'):
        base_url = base_url or self._base_url
        url:str = f'{base_url}/{api_version}{path}'
        headers:dict= {'APCA-API-KEY-ID':self._api_key,'APCA-API-SECRET-KEY':self._secret_key}
        retry = self._retry
        if retry < 0:
            retry = 0
        while retry>=0:
            try:
                return self._one_request(method,url,headers,retry)
            except RetryException:
                retry_wait = self._retry_wait
                logger.warning(f'sleep {retry_wait} seconds and retrying {url} {retry} more times')
                time.sleep(retry_wait)
                retry-=1
                continue
    
    def _one_request(self,method:str, url:str,headers:dict,retry:int):
        retry_codes = self._retry_codes
        resp = self._session.request(method=method,url=url,headers=headers)
        try:
            resp.raise_for_status()
        except HTTPError as http_error:
            if resp.status_code in retry_codes and retry > 0:
                raise RetryException()
            if 'code' in resp.text:
                error = resp.json()
                if 'code' in error:
                    raise APIError(error,http_error)
            else:
                raise
        if resp.text!='':
            return resp.json()
        return None
    
    def get(self,path,headers=None):
        return self._request('GET',path,headers)
    
    def get_account(self) -> Account:
        resp = self.get('/account')
        return Account(resp)


    def get_orders(self,
    status: str = None,
    limit : str = None,
    after : str = None,
    until : str = None,
    direction : str = None,
    nested : str = None,
    symbols: str = None
    ) -> Orders:
        if params is None:
            params = {}
        if status is None:
            param['status'] = status
        if limit is not None:
            params['limit'] = limit
        if after is not None:
            params['after'] = after
        if until is not None:
            params['until'] = until
        if direction is not None:
            params['direction'] = direction
        if nested is not None:
            params['nested']  = nested
        if symbols is not None:
            params['symbol'] = symbols
        resp = self.get('/orders',params)
        return [Order(o) for o in resp]
            
                    

         
    