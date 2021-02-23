# tuples: ordered, immutable, allows duplicate, faster than list
# creating tuple
import timeit
import sys
t1 = ('adnan', 28)
t2 = 'adnan', 28
t3 = ('kayace',)
not_tuple = ("Turkey")
t4 = tuple([1, 2, 3])

print(t1, t2, t3, t4, not_tuple)
print(f"first item: {t1[0]}")
print(f"last item: {t1[-1]}")

# t1[0] = "ADNAN"  # TypeError: 'tuple' object does not support item assignment
for data in t1:
    print(data)

if 'adnan' in t1:
    print('yes adnan here')
else:
    print('adnan NOT here')

tp = ('a', 'a', 'b', 'b', 'c', 'd', 'e', 'e', 'e')
print(f"len(tp): {len(tp)}")  # 9
print(f"tp.count('e'): {tp.count('e')}")  # tp.count('e'): 3
print(f"tp.index('e'): {tp.index('e')}")  # 6
tn = (1, 4, 5, 6, 7, 8, 9)
tn1 = tn[:3]
tn2 = tn[3:]
tn3 = tn[2:5]
print(tn1, tn2, tn3)  # (1, 4, 5) (6, 7, 8, 9) (5, 6, 7)
tn_rev = tn[::-1]
print(f"tn_rev: {tn_rev}")  # tn_rev: (9, 8, 7, 6, 5, 4, 1)

mt = 'adnan', 'kaya', 28
fname, lname, age = mt
print(mt)
print(fname, lname, age)
nums = (1, 2, 3, 4, 5, 6, 7)
i1, *i2, i3 = nums
print(f"nums : {nums}")
print(f"i1 : {i1}, i3: {i3}")  # i1 : 1, i3: 7
print(f"i2 : {i2}")  # i2 : [2, 3, 4, 5, 6] # !! list
# compare tuple vs list
mlist = [0, 1, 2, 'selam', True]
mtuple = (0, 1, 2, 'selam', True)
print(sys.getsizeof(mlist), 'bytes')  # 120 bytes
print(sys.getsizeof(mtuple), 'bytes')  # 80 bytes
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1_000_000)) # 0.07721824799955357
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1_000_000)) # 0.014095197999267839
