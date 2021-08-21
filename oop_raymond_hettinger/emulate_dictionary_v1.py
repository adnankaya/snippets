# Project: Emulating how dictionaries work
# Variables: n, key_arr, val_arr
# Namespace: globals
# Execution technique: functions
# Limitations: In one namespace a variable name can be used only once
# Engineering Problem: One namespace is not good enough

def setup():
    global N, key_arr, val_arr
    N = 8
    key_arr = [[] for i in range(N)]
    val_arr = [[] for i in range(N)]

def store(key, value):
    i = hash(key) % N
    key_arr[i].append(key)
    val_arr[i].append(value)

def lookup(key):
    i = hash(key) % N
    try:
        k = key_arr[i].index(key)
    except ValueError:
        raise KeyError(key)
    # import pdb;pdb.set_trace()
    # print(f'val_arr : {val_arr}')
    return val_arr[i][k]

if __name__=='__main__':
    setup()
    store('adnan','kaya')
    store('ali','veli')
    store('ömer','adil')
    print(lookup('adnan'))