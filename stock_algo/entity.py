import pandas as pd
import pprint
import re

ISO8601YMD = re.compile(r'\d{4}-\d{2}-\d{2}T')
NY = 'America/New_York'


class Entity(object):
    '''This helper class provides property access (the "dot notation")
    to the json object, backed by the original object stored in the _raw
    field.
    '''

    def __init__(self, raw):
        self._raw = raw

    def __getattr__(self, key):
        if key in self._raw:
            val = self._raw[key]
            if (isinstance(val, str) and
                    (key.endswith('_at') or
                     key.endswith('_timestamp') or
                     key.endswith('_time')) and
                    ISO8601YMD.match(val)):
                return pd.Timestamp(val)
            else:
                return val
        return super().__getattribute__(key)

    def __repr__(self):
        return '{name}({raw})'.format(
            name=self.__class__.__name__,
            raw=pprint.pformat(self._raw, indent=4),
        )


class Account(Entity):
    """
    Entity properties:
    https://alpaca.markets/docs/api-documentation/api-v2/account/
    """
    pass