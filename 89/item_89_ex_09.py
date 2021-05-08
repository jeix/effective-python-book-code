# page 616

# python3 item_89_ex_09.py

import warnings

try:
    warnings.warn('This usage is deprecated', DeprecationWarning)
except DeprecationWarning:
    print('DeprecationWarning caught')
