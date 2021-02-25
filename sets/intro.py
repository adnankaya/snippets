# sets: unordered, mutable, no duplicates
s = {1, 2, 3, 1, 2, 3}
print(f"s: {s}")
s2 = {"adnan", 23, 46.55, True, False, "adnan", "kayace"}
print(f"s2: {s2}")

h = set("adnan kayace")
print(f"h: {h}")

s3 = {1, 2, 3}
print(f"s3:{s3}")
s3.add(4)
print(f"s3:{s3}")
s3.remove(2)
print(f"s3:{s3}")
s3.discard(1)
print(f"s3:{s3}")
print(f"s3.pop(): {s3.pop()}, {s3}")
# s3.clear() # to empty the set

s4 = {7, 8, 9}
for i in s4:
    print(i, end=",")
if 8 in s4:
    print("\n8 in s4")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
print(f"odds.union(primes): {odds.union(primes)}")
print(f"odds.intersection(evens): {odds.intersection(evens)}")
print(f"odds.intersection(primes): {odds.intersection(primes)}")

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12, 13}
print(f"setA.difference(setB): {setA.difference(setB)}")
print(f"setB.difference(setA): {setB.difference(setA)}")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12, 13}
print(f"setA.symmetric_difference(setB): {setA.symmetric_difference(setB)}")
print(f"setB.symmetric_difference(setA): {setB.symmetric_difference(setA)}")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12, 13}
print(f"setA.update(setB): {setA.update(setB)} |> new setA: {setA}")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12, 13}
print(
    f"setA.intersection_update(setB): {setA.intersection_update(setB)} |> new setA: {setA}")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12, 13}
print(
    f"setA.difference_update(setB): {setA.difference_update(setB)} |> new setA: {setA}")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12, 13}
print(
    f"setA.symmetric_difference_update(setB): {setA.symmetric_difference_update(setB)} |> new setA: {setA}")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}
print(f"setB.issubset(setA): {setB.issubset(setA)}")
print(f"setB.issuperset(setA): {setB.issuperset(setA)}")
setB = {1, 2, 3}
setC = {1, 5, 77}
setD = {99}
print(f"setB.isdisjoint(setC): {setB.isdisjoint(setC)}")
print(f"setB.isdisjoint(setD): {setB.isdisjoint(setD)}")
set1 = {1, 2, 3}
# set2 = set1 # !DANGEROUS
set2 = set1.copy()  # to copy: 1.way
set2 = set(set1)  # to copy: 2.way
set2.add(44)
print(f"set1, set2: {set1, set2}")

fs = frozenset([1, 2, 3, 3, 4])  # immutable set
print(f"frozenset: {fs}")
# fs.add(46)  # ERROR
# fs.append(46) # ERROR
