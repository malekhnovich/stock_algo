import logging
import os
from requests.exceptions import HTTPError
import time
from config import base_url,api_key,secret_key


logger = logging.getLogger(__name__)

class RetryException(Exception):
    pass
class APIError(Exception):
    def __init__(self,error,http_error=None):
        super().__init__(error['message'])
        self._error = error
        self._http_error = http_error