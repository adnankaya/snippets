import time
def compute1(limit):
    res = []
    for i in range(limit):
        res.append(i)
    return res


def compute2(limit):
    for i in range(limit):
        yield i

t1s = time.perf_counter()
compute1(1_000_000)
t1e = time.perf_counter()
print(f"compute1 duration: {t1e-t1s}")
t2s = time.perf_counter()
compute2(1_000_000)
t2e = time.perf_counter()
print(f"compute2 duration: {t2e-t2s}")