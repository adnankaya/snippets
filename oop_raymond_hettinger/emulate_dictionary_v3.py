# Project: Emulating how dictionaries work
# Variables: n, key_arr, val_arr
# Namespace: simple namespace
# Execution technique: functions
# Benefit: we can have multiple namespaces
# Problem: Every new case, we have to manually create a new simple namespace
# Problem2: Every single call to the function has to manually pass in
# the namespace for us.
# Solution : Python OOP's classes

from types import SimpleNamespace


def setup(ns):
    ns.n = 8
    ns.key_arr = [[] for i in range(ns.n)]
    ns.val_arr = [[] for i in range(ns.n)]


def store(ns, key, value):
    i = hash(key) % ns.n
    ns.key_arr[i].append(key)
    ns.val_arr[i].append(value)


def lookup(ns, key):
    i = hash(key) % ns.n
    try:
        k = ns.key_arr[i].index(key)
    except ValueError:
        raise KeyError(key)

    return ns.val_arr[i][k]


if __name__ == '__main__':
    ns1 = SimpleNamespace()
    setup(ns1)
    store(ns1, 'adnan', 'kaya')
    store(ns1, 'ali', 'veli')
    store(ns1, 'ömer', 'adil')
    print(lookup(ns1, 'adnan'))
    ns2 = SimpleNamespace()
    setup(ns2)
    store(ns2, 'adnan', '23')
    store(ns2, 'ali', '12')
    store(ns2, 'ömer', '33')
    print(lookup(ns2, 'adnan'))
