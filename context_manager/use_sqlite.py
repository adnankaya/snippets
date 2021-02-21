from sqlite3 import connect

"""
class TemptableContextManager():
    def __init__(self, gen):
        self.gen = gen

    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self

    def __enter__(self):
        print("enter")
        self.gen_instance = self.gen(*self.args, **self.kwargs)
        next(self.gen_instance)

    def __exit__(self, *args):
        print("exit")
        next(self.gen_instance, None)
"""

# @TemptableContextManager
from contextlib import contextmanager
@contextmanager
def temptable_generator(cur):
    cur.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        cur.execute("drop table points")


# temptable_generator = TemptableContextManager(temptable_generator)

with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable_generator(cur):
        cur.execute('insert into points(x,y) values(1,1)')
        cur.execute('insert into points(x,y) values(1,2)')
        cur.execute('insert into points(x,y) values(2,1)')
        for row in cur.execute("select x,y from points"):
            print(row)
        for row in cur.execute("select sum(x*y) from points"):
            print("sum: ", row)
