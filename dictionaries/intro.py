# dictionaries: unordered, key-value pairs, mutable
"""
md1 = {"fname": "adnan", "age": 28}
md2 = dict(fname='murat', age=24, job='civil engineer')
print(md1)
print(md2)
print(f"md1['fname']:{md1['fname']}")
md1["email"] = "kayace.info@gmail.com"
print(md1)
md1["email"] = "kayace.info@example.com"
print(md1)
del md1["email"]
print("del md1['email']: ", md1)
md1.pop('age')
print("md1.pop('age')", md1)
print(f"md2.popitem() >>> popitem: {md2.popitem()}: md2: {md2}")
if 'age' in md2:
    print(f"md2['age']: {md2['age']}")
else:
    print('age doesnot exist in md2')

for k, v in md2.items():
    print(f"{k}->{v}")

print(f"md2: {md2}")
md2new = md2  # DANGEROUS! # use md2.copy() or dict(md2)
md2new['email'] = 'murat@kayaceins.com'
print(f"md2: {md2}")
print(f"md2new: {md2new}")
"""
md1 = {"fname": "adnan", "age": 28}
print(f"md1: {md1}")
md2 = dict(fname='murat', age=24, job='civil engineer')
print(f"md2: {md2}")
md1.update(md2)
print(f"md1: {md1}")
mdnums = {23: 44, 67: 46}
print(f"mdnums: {mdnums}")
print(f"mdnums[67]: {mdnums[67]}")
mtuple = (46, 57)
mdict = {mtuple: 1000}
print(f"mdict: {mdict}")
mlist = [88, 77]
# mdict2 = {mlist: 1111}  # TypeError: unhashable type: 'list'
# print(f"mdict2: {mdict2}")
