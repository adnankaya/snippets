# Project: Emulating how dictionaries work
# Variables: n, key_arr, val_arr
# Namespace: Dict class
# Execution technique: class , instance functions
# Benefit: we can have multiple namespaces
# Problem: we need to write method names, writing them too hard :D
# Solution: change the method names so we can use operators

class Dict:

    def setup(self):
        self.n = 8
        self.key_arr = [[] for i in range(self.n)]
        self.val_arr = [[] for i in range(self.n)]

    def store(self, key, value):
        i = hash(key) % self.n
        self.key_arr[i].append(key)
        self.val_arr[i].append(value)

    def lookup(self, key):
        i = hash(key) % self.n
        try:
            k = self.key_arr[i].index(key)
        except ValueError:
            raise KeyError(key)

        return self.val_arr[i][k]


if __name__ == '__main__':
    d1 = Dict()
    d1.setup()
    d1.store('adnan', 'kaya')
    d1.store('ali', 'veli')
    d1.store('ömer', 'adil')
    print(d1.lookup('adnan'))
    d2 = Dict()
    d2.setup()
    d2.store('adnan', '23')
    d2.store('ali', '12')
    d2.store('ömer', '22')
    print(d2.lookup('adnan'))
