# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

mstr = 'aaaaaabbbcccddddd'
mc = Counter(mstr)
print(f"mycounter: {mc}")
print(f"mycounter.items(): {mc.items()}")
print(f"mycounter.elements(): {list(mc.elements())}")
print(f"mycounter.keys(): {mc.keys()}")
print(f"mycounter.values(): {mc.values()}")
print(f"mycounter.most_common(): {mc.most_common(1)}")  # most common 1 element
print(f"mycounter.most_common(): {mc.most_common(2)}")  # most common 2 element
############ named tuple #############
print("----------------namedtuple---------------")
Point = namedtuple('Point', 'x,y,z')
p1 = Point(44, 23, 34)
print(f"p1: {p1}")
print(f"p1.x, p1.y, p1.z --> {p1.x} {p1.y} {p1.z}")
############ OrderedDict #############
# OrderedDict: remembers the order of data when it was inserted
# in python3.7 normal dictionary also remembers the order of data when it was inserted
print("----------------OrderedDict---------------")
ord_dict = OrderedDict()
ord_dict['b'] = 2
ord_dict['c'] = 33
ord_dict['d'] = 44
ord_dict['a'] = 1
print(f"ord_dict: {ord_dict}")
############ default dict #############
# we define the type of dict and it gives default value to the keys
# we assign different type rather than default type
print("----------------defaultdict---------------")
dd1 = defaultdict(int)
dd2 = defaultdict(float) # float, string, list, tuple, dict
dd1['a'] = 23
dd1['b'] = 44
print(f"dd1: {dd1} ------>  dd1['c']: {dd1['c']}")
print(f"dd2['i']: {dd2['i']} ")
############ deque #############
# 
print("----------------deque---------------")

d = deque()
d.append(23)
d.append(44)
print(f"d: {d}")
d.appendleft(34)
print(f"d: {d}")
d.pop()
print(f"d: {d}")
d.popleft()
print(f"d: {d}")
d.clear()
print(f"d: {d}")
d.extend([2,0,7,4])
print(f"d: {d}")
d.extendleft([100,1001])
print(f"d: {d}")
# rotate right by passing positive numbers, for left negative numbers
print(f"d.rotate(1): {d.rotate(1)}, rotated: {d}")
print(f"d.rotate(2): {d.rotate(2)}, rotated: {d}")
print(f"d.rotate(-3): {d.rotate(-3)}, rotated: {d}")