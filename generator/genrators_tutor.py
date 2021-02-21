def square_nums(nums):
    for i in nums:
        yield i*i


res = square_nums([1, 2, 3, 4, 5])

# print(next(res)) # 1
# print(next(res)) # 4
# print(next(res)) # 9
# print(next(res)) # 16
# print(next(res)) # 25
# print(next(res)) # StopIteration exception
for r in res:
    print(r)

# paranthesis () makes as generator
# squared [] paranthesis makes as list
gen2 = (x*x for x in [1,2,3,4,5]) 
print("gen2: ",type(gen2))

