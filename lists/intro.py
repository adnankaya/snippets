# Lists: ordered, mutable, allows duplication, can contain different types of datas
"""
li = ["muz", 23, True, 'elma', 'elma']
print(li)
print(f"first element: {li[0]}")
print(f"last element: {li[-1]}")
## print(li[5]) # IndexError: list index out of range
if 'muz' in li:
    print('muz var')
else:
    print('muz yok')

print(f"len(li): {len(li)}")
li.append('karpuz')
print(f"li.append('karpuz'):{li}")
li.insert(2, 'new_element')
print(f"li.insert(index, new_element): {li}")
# remove last element 
last_item = li.pop()
print(f"last item removed with li.pop(): {li}")
# remove specific item
removed = li.remove('elma') # ilk buldugu elmayi siler
print(f"li.remove('elma') removed:{removed}, li:{li}")
# clear all elements
li.clear()
print(f"li.clear(): {li}")

li = ['adnan', 'kaya', 'ce']
li_reversed = li.reverse()
# li_reversed: None , li.reverse():['ce', 'kaya', 'adnan']
print(f"li_reversed: {li_reversed} , li.reverse():{li}")
li_sorted = li.sort()
# li_sorted: None , li.sort():['adnan', 'ce', 'kaya']
print(f"li_sorted: {li_sorted} , li.sort():{li}")
li = ['adnan', 'kaya', 'ce']
sortedli = sorted(li)
# li: ['adnan', 'kaya', 'ce'], sorted(li): ['adnan', 'ce', 'kaya']
print(f"li: {li}, sorted(li): {sortedli}")
zeros = [0] * 3
ones = [1] * 5
print(f"zeros:{zeros}, ones: {ones}")  # zeros:[0, 0, 0], ones: [1, 1, 1, 1, 1]
zeros_ones = zeros + ones
print(f"zeros_ones: {zeros_ones}")  # zeros_ones: [0, 0, 0, 1, 1, 1, 1, 1]
li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# slicing
sliced = li[2:5]
print(f"li[2:5] sliced: {sliced}")  # sliced: [2, 3, 4]
print(f"li[:5]: {li[:5]}")  # li[:5]: [0, 1, 2, 3, 4]
print(f"li[4:]: {li[4:]}")  # li[4:]: [4, 5, 6, 7, 8, 9]
print(f"li[::1]: {li[::1]}")  # li[::1]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"li[::2]: {li[::2]}")  # li[::2]: [0, 2, 4, 6, 8]
print(f"li[::-1]: {li[::-1]}")  # li[::-]: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f"li[::-2]: {li[::-2]}")  # li[::-2]: [9, 7, 5, 3, 1]
origlist = ["a","b","c"]
newlist = origlist # DANGEROUS! both list points the same address on memory
print(f"origlist: {origlist}")
print(f"newlist: {newlist}")
newlist.append('x')
print(f"origlist: {origlist}")
print(f"newlist: {newlist}")
########## these 3 copying style are same #########
copiedlist = origlist.copy() # 1.
copiedlist = list(origlist) # 2.
copiedlist = origlist[:] # 3.
###################################################
print(f"origlist: {origlist}")
print(f"copiedlist: {copiedlist}")
copiedlist.append('haha')
print(f"copiedlist: {copiedlist}")
print(f"origlist: {origlist}")
"""
# list comprehension
li = [1,2,3,4,5]
print(f"li: {li}")
newli = [i for i in li]
print(f"newli: {newli}")
li_power2 = [i**2 for i in li]
print(f"li_power2: {li_power2}")
