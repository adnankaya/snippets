from collections import ChainMap


class P:
    x = 10
    y = 20
    z = 30


class C(P):
    y = 202
    z = 303

a = C()
a.z = 6666

b = C()
b.z = 7777

ma = ChainMap(vars(a), vars(C), vars(P))
mb = ChainMap(vars(b), vars(C), vars(P))