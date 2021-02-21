from time import sleep

# def compute1(limit):
#     res = []
#     for i in range(limit):
#         sleep(0.5) # wait for 1/2 second
#         res.append(i)
#     return res

# print(compute1(10)) # will display values after 5 seconds

def compute2(limit):
    for i in range(limit):
        sleep(0.5)
        yield i

for result in compute2(10):
    print(result)