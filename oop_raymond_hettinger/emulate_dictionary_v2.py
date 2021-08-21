# Project: Emulating how dictionaries work
# Variables: n, key_arr, val_arr
# Namespace: user dicts, globals
# Execution technique: functions
# Benefit: we can have multiple namespaces
# Problem: ns['varr'] looks ugly
# Solution is simple namespaces

def setup(ns):
    ns['N'] = 8
    ns['key_arr'] = [[] for i in range(ns['N'])]
    ns['val_arr'] = [[] for i in range(ns['N'])]

def store(ns, key, value):
    i = hash(key) % ns['N']
    ns['key_arr'][i].append(key)
    ns['val_arr'][i].append(value)

def lookup(ns, key):
    i = hash(key) % ns['N']
    try:
        k = ns['key_arr'][i].index(key)
    except ValueError:
        raise KeyError(key)

    return ns['val_arr'][i][k]

if __name__=='__main__':
    ns1 = {}
    setup(ns1)
    store(ns1, 'adnan','kaya')
    store(ns1, 'ali','veli')
    store(ns1, 'ömer','adil')
    print(lookup(ns1, 'adnan'))
    ns2 = {}
    setup(ns2)
    store(ns2, 'adnan','29')
    store(ns2, 'ali','22')
    store(ns2, 'ömer','32')
    print(lookup(ns2, 'adnan'))
    
    ns_globals = globals()
    setup(ns_globals)
    store(ns_globals, 'adnan','red')
    store(ns_globals, 'ali','blue')
    store(ns_globals, 'ömer','yellow')
    print(lookup(ns_globals, 'adnan'))