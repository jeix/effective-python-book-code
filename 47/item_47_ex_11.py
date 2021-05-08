# page 304

class BrokenDictionaryRecord:
    def __init__(self, data):
        self._data = {}

    def __getattribute__(self, name):
        print(f'* Called __getattribute__({name!r})')
        return self._data[name]

data = BrokenDictionaryRecord({'foo': 3})
data.foo

# * Called __getattribute__('foo')
# * Called __getattribute__('_data')
# ... (992)
# * Called __getattribute__('_data')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 7, in __getattribute__
#   File "<stdin>", line 7, in __getattribute__
#   File "<stdin>", line 7, in __getattribute__
#   [Previous line repeated 992 more times]
#   File "<stdin>", line 6, in __getattribute__
# RecursionError: maximum recursion depth exceeded while calling a Python object
# * Called __getattribute__('_data')
