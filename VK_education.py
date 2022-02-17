# import pytest

def tuple_check(item):
    result = type((item, ))
    return result

def int_check(value):
    result = type(int(value))
    return result
