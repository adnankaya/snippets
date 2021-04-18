import abc

class Double(metaclass=abc.ABCMeta):
    pass


print(isinstance(float(1.213), Double)) # False
Double.register(float) # float is virtual subclass of Double now!
print(Double.__mro__)
print("issubclass(float, Double): ",issubclass(float, Double)) # True
print(isinstance(float(1.213), Double)) # True

# The decorator register method helps you to create a hierarchy of custom virtual class inheritance.
@Double.register
class Double64:
    """A 64-bit double-precision floating-point number."""
    pass

print("Double64",issubclass(Double64, Double))  # True