# Project: Emulating how dictionaries work
# Variables: n, key_arr, val_arr
# Namespace: Dict class
# Execution technique: class, instace functions
# Benefit: we can have multiple namespaces
# Problem:

class Dict:

    def __init__(self):
        self.n = 8
        self.key_arr = [[] for i in range(self.n)]
        self.val_arr = [[] for i in range(self.n)]

    def __setitem__(self, key, value):
        i = hash(key) % self.n
        self.key_arr[i].append(key)
        self.val_arr[i].append(value)

    def __getitem__(self, key):
        i = hash(key) % self.n
        try:
            k = self.key_arr[i].index(key)
        except ValueError:
            raise KeyError(key)

        return self.val_arr[i][k]


if __name__ == '__main__':
    d1 = Dict()

    d1['adnan'] = 'kaya'
    d1['ali'] = 'veli'
    d1['ömer'] = 'adil'
    print(d1['adnan'])
