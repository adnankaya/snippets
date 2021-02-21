from time import sleep

def compute1(limit):
    result = []
    for i in range(limit):
        sleep(0.5) # yarim saniye bekle
        result.append(i)
    return result

print(compute1(10)) # 5 saniye sonra result gelecek

def compute2(limit):
    for i in range(limit):
        sleep(0.5)
        yield i

for c2 in compute2(10):
    print(c2) # yarim saniyede bir degerleri tek tek goster