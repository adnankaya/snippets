from contextlib import contextmanager

@contextmanager
def open_file(mfile, mode):
    f = open(mfile, mode)
    yield f
    f.close()
with open_file('sample_func.txt','w') as of:
    of.write("hello for context manager using with method")


print(of.closed)