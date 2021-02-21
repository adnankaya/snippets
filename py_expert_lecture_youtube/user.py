from library import Base

# check if Base has foo method, if not raise error
# assert hasattr(Base, 'foo'), 'there is no foo'
class Derived(Base):
    # def bar(self):
    #     return "bar"
    pass

# d = Derived()
# print(d.bar())