# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat
# from itertools import infinite
import operator

li1 = [1, 2]
li2 = [44]
prod1 = product(li1, li2, repeat=1)
prod2 = product(li1, li2, repeat=2)
# print(f"list(prod1): {list(prod1)}")
print(f"list(prod2): {list(prod2)}")
############ permutations #############
print("----------------permutations---------------")
mlist = [1, 2, 3]
perm1 = permutations(mlist)
perm2 = permutations(mlist, 2)
print(f"permutations with length default: {list(perm1)}")
print(f"permutations with length 2: {list(perm2)}")
############ combinations #############
print("----------------combinations---------------")
mlist = [1, 2, 3, 4]
comb1 = combinations(mlist, 2)
comb_wr = combinations_with_replacement(mlist, 2)
print(f"combinations with length 2: {list(comb1)}")
print(f"combinations_with_replacement: {list(comb_wr)}")
############ accumulate #############
print("----------------accumulate---------------")
l = [1, 2, 5, 3, 4]
print(f"l: {l}")
acc1 = accumulate(l)  # default is 'sum' operation
print(f"acc1: {list(acc1)}")
acc2 = accumulate(l, func=operator.mul)  # mul: multiply
print(f"acc2: {list(acc2)}")
acc3 = accumulate(l, func=max)  # max: getting max number
print(f"acc3: {list(acc3)}")
############ groupby #############
print("----------------groupby---------------")
mlist = [1, 2, 3, 4, 6, 7, 8, 9, 11, 13]

group_obj = groupby(mlist, key=lambda val: val % 2 != 0)
for key, value in group_obj:
    print(f"is {list(value)} odd number ? :{key}")
print()
persons = [
    {'name': 'Adnan', 'age': 28},
    {'name': 'Davud', 'age': 24},
    {'name': 'Ibrahim', 'age': 30},
    {'name': 'Abdullah', 'age': 30}
]
groupby_age = groupby(persons, key=lambda p: p['age'])
for key, value in groupby_age:
    print(f"{key} {list(value)}")

############ count, cycle, repeat #############
print("----------------count, cycle, repeat---------------")
# count: for infinite
for i in count(10):  # start from 10
    print(i, end=',')
    if i == 15:
        break

# cycle : through a list
mlist = [1, 2, 3, 4]
c = 0
for i in cycle(mlist):
    print(i, end='\t')
    c += 1
    if c > 20:
        break

for i in repeat(1, 4): # repeat number 1, for 4 times
    print(i)
