import logging
import os
from typing import List
from requests.exceptions import HTTPError
from config import (
    base_url,
    api_key,
    secret_key
)

logger = logging.getLogger(__name__)

class RetryException(Exception):
    pass

class APIError(Exception):
    """
    Represents API related error
    Args:
        Exception ([type]): [description]
    """
    def __init__(self,error,http_error=None):
        super().__init__(error['message'])
        self._error = error
        self._http_error = http_error
    
    @property
    def code(self):
        return self._error['code']
    
     @property
    def status_code(self):
        http_error = self._http_error
        if http_error is not None and hasattr(http_error, 'response'):
            return http_error.response.status_code

    @property
    def request(self):
        if self._http_error is not None:
            return self._http_error.request

    @property
    def response(self):
        if self._http_error is not None:
            return self._http_error.response
    
    class REST(object):
        def __init(self, key_id:str = api_key,
        secret_key:str = api_secret,
        base_url:str =None):

        self.key_id =  
