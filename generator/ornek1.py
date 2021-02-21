def compute(limit):
    for i in range(1, limit+1):
        yield i*i


res = compute(5)
# Verilere erisim 1. yontem
# print(next(res))  # 1
# print(next(res))  # 4
# print(next(res))  # 9
# print(next(res))  # 16
# print(next(res))  # 25
# print(next(res)) # StopIteration exception


# Verilere erisim 2. yontem
# for r in res:
#     print(r)
for r in res:
    print(r, end='\t')
