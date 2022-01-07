

def coro1():
    while d := (yield 'send 1 or None to exit'):
        print(f'coro1 -> d:{d}')


def coro2():
    while d := (yield 'send 2 or None to exit'):
        print(f'coro2 -> d:{d}')


c1 = coro1()
next(c1)
c1.send(100)  # coro1 -> d:100
c1.send(111)  # coro1 -> d:111
print('-'*60)
c2 = coro2()
next(c2)
c2.send(200)  # coro2 -> d:200
c2.send(222)  # coro2 -> d:222


def combined_coro():
    while d := (yield 'SELECT 1 or 2 or None to exit'):
        if d == 1:
            print('selected coro1')
            yield from coro1()
        elif d == 2:
            print('selected coro2')
            yield from coro2()
        else:
            output = 'Unknown choice'


print('_______Combined Coroutine_______')
cc = combined_coro()
next(cc)
cc.send(1)  # we have chosen coro1
cc.send(11)
cc.send(111)
print(cc.send(None)) # we exited from coro1
cc.send(2) # we have chosen coro2
"""
 └─ λ python yield_from.py 
coro1 -> d:100
coro1 -> d:111
------------------------------------------------------------
coro2 -> d:200
coro2 -> d:222
_______Combined Coroutine_______
selected coro1
coro1 -> d:11
coro1 -> d:111
SELECT 1 or 2 or None to exit
selected coro2
"""