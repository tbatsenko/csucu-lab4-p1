# File: test_except.py
# This module tests a func.py module
from func import *

for item in [KeyError, IndexError, MyError, None]:
    except_func(item)
