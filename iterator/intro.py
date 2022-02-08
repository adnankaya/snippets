
class myrange(object):
    '''
    This is an iterator which 
    implements __next__ method and 
    implements __iter__ method that returns itself
    '''

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current


nums = myrange(1, 10)
for num in nums:
    print(num, end='\t')

print()
print('_'*70)
def mygen(start, end, step=1):
    while start < end:
        yield start
        start += step

nums = mygen(1, 10)
for num in nums:
    print(num, end='\t')
print()
"""
 └─ λ python intro.py 
1       2       3       4       5       6       7       8       9
______________________________________________________________________
1       2       3       4       5       6       7       8       9
"""