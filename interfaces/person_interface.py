class PersonMeta(type):
    def __instancecheck__(cls, instance):
        """when you use isinstance() this method will be called"""
        return cls.__subclasscheck__(type(instance))
    
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name')and
        callable(subclass.name)and
        hasattr(subclass,'age')and
        callable(subclass.age))

class InterfacePerson(metaclass=PersonMeta):
    """InterfacePerson interface built from PersonMeta metaclass."""
    pass

class PersonSuper:
    '''This super class is also implemented InterfacePerson Interface '''
    def name(self) -> str:
        pass
    def age(self) -> int:
        pass

class Employee(PersonSuper):
    pass

class Friend:
    def name(self):
        pass
    def age(self):
        pass

print("employee: ", issubclass(Employee, InterfacePerson)) # True
print("friend: ", issubclass(Friend, InterfacePerson)) # True

print(Employee.__mro__) # (<class '__main__.Employee'>, <class '__main__.PersonSuper'>, <class 'object'>)
print(Friend.__mro__) # (<class '__main__.Friend'>, <class 'object'>)

print(isinstance(Friend(), InterfacePerson)) # True