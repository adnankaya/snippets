class A:
    def __init__(self):
        print('init A')


class B:
    def __init__(self):
        print('init B')


class C():
    def __init__(self):
        super().__init__()
        print('init C')


class D(B, A, C):
    def __init__(self):
        super().__init__()  # init B
        super(B, self).__init__()  # init A
        super(A, self).__init__()  # init C
        print('wow init D')


c = C()
print("--------------------")
d = D()

print("--------------------")
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>)
print(D.__mro__)
