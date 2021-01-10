import os

class FLOAT(str):
    def __new__(cls,value):
        if isinstance(value,float) or isinstance(value,int):
            return value
        if isinstance(value,str):
            return float(value.strip())
        raise ValueError(f'Unexpected float format {value}')