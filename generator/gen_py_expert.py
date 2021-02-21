import time


def compute():
    rv = []
    for i in range(10):
        time.sleep(.5)
        rv.append(i)
    return rv


class Compute:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last >= 10:
            raise StopIteration()
        time.sleep(.5)
        return rv


def compute_gen():
    for i in range(10):
        time.sleep(.5)
        yield i

# computed_gens = compute_gen()
# for i in computed_gens:
#     print(i)


class Api:
    '''we can not guarantee an Api user will run these in order '''

    def run_this_first(self):
        self.first()

    def run_this_second(self):
        self.second()

    def run_this_last(self):
        self.last()


def first(): print('first works')
def second(): print('second works')
def last(): print('last works')


def api():
    '''Enforces user of this method to run 
    the following methods in order '''
    first()
    yield
    second()
    yield
    last()
    yield
