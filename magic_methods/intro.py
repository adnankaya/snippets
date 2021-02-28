

class Employee():
    raise_amount = 1.04

    # def __new__(cls):
    #     print('new method worked')
    #     return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        '''for unambigous representation,
        used for debugging, logging '''
        return f"Employee({self.name}, {self.age})"

    def __str__(self):
        '''used for to display the information to the end-user '''
        return f"{self.name} {self.age}"

    def __add__(self, other):
        # when 2 instances are having addition
        if isinstance(other, Employee):
            return self.age + other.age

    def __sub__(self, other):
        # when 2 instances are having substraction
        if isinstance(other, Employee):
            return self.age - other.age

    def __mul__(self, other):
        # when 2 instances are having multiply opr.
        if isinstance(other, Employee):
            return self.name * (other.age % 10)

    def __call__(self):
        # Called when the instance is “called” as a function
        return f"<Employee {self.name} called!>"

    def __len__(self):
        return len(self.name)


e1 = Employee('adnan', 28)
e2 = Employee('murat', 24)
# print(e1) # <__main__.Employee object at 0x7f5fb940ffd0>
print(repr(e1))  # or e1.__repr__()
print(str(e1))  # or e1.__str__()
print(e2.__repr__())
print(e2.__str__())
print(f"sum of age: {e1 + e2}")
print(f"substraction of age: {e1 - e2}")
print(f"mul of age: {e1 * e2}")
print(f"call e1: {e1()}")
print(f"len of e1: {len(e1)}")  # can use e1.__len__()
