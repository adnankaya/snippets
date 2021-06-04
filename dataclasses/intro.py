from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    name: str
    age: int
    strength: int = 100
    sort_index: str = field(init=False, repr=False)

    def __post_init__(self):
        # self.sort_index = self.name # if frozen=True, we can not assign
        object.__setattr__(self, 'sort_index', self.strength)


p1 = Person("aaac", 29)
p2 = Person("aaad", 25)

print(p1)
# p1.name = 'new name' # dataclasses.FrozenInstanceError: cannot assign to field 'name'
print(p2 > p1)  # compares order number of charachter in alphabet
"""
sort_index: used as a sorting parameter, not as a class variable

"""
