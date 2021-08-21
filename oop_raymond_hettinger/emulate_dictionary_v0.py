# Project: Emulating how dictionaries work
# Variables: n, key_arr, val_arr
# Namespace: globals
# Execution technique: manually typing

"""
>>> type(globals())
<class 'dict'>

>>> globals()['i'] = 123
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'i': 123}
>>> globals()['i']
123

>>> d = dict()
>>> d['adnan']='kaya'
>>> d
{'adnan': 'kaya'}

>>> from types import SimpleNamespace
>>> ns = SimpleNamespace(x=11,y=22)
>>> ns.x
11
>>> ns.y
22

>>> #Emulating dictionaries
>>> n = 8
>>> key_arr = [[] for i in range(n)]
>>> val_arr = [[] for i in range(n)]
>>> 
>>> key, value = 'adnan', 'kaya'
>>> 
>>> i = hash(key) % n
>>> i
6
>>> key_arr
[[], [], [], [], [], [], [], []]
>>> val_arr
[[], [], [], [], [], [], [], []]
>>> key_arr[i].append(key)
>>> val_arr[i].append(value)

>>> key_arr
[[], [], [], [], [], [], ['adnan'], []]
>>> val_arr
[[], [], [], [], [], [], ['kaya'], []]
>>> 
"""
