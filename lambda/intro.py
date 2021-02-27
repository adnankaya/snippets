# usage;  lambda: params: expression

# pol = lambda x,y,z: x**2+y+z
# print(pol(3, 1, 4))

from functools import reduce
points2D = [(1, 2), (15, 1), (5, -1), (10, 8)]
# sort by second element
points2D_sorted1 = sorted(points2D)
points2D_sorted2 = sorted(points2D, key=lambda x: x[1])
# sort by sum of each tuple
points2D_sorted3 = sorted(points2D, key=lambda x: x[0]+x[1])
print(points2D)
print("sort by x ", points2D_sorted1)
print("sort by y ", points2D_sorted2)
print("sort by x+y ", points2D_sorted3)

print("-------------map -------------")
# map(func, sequence)
a = [1, 2, 3, 4, 5, 6]
b = map(lambda i: i*i, a)
print(a)
print(tuple(b))
print("-------------list comprehension -------------")
a = [1, 2, 3, 4, 5, 6]
c = [i**i for i in a]
print(c)
print("-------------filter -------------")
# filter(func, sequence) # returns True or False
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda i: i % 2 == 0, a)
print(a)
print(tuple(b))
c = [i for i in a if i % 2 == 0]
print(c)
print("-------------reduce -------------")
# reduce(func, sequence) # returns single value
a = [1, 2, 3, 4, 5, 6]
multiplied_values = reduce(lambda i,j: i*j, a)
print(a)
print(multiplied_values)

