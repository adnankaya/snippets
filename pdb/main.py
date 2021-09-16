from helper import timer, compute, foo, long_dict


class Person:
    def __init__(self, username, website):
        self.username = username
        self.website = website


@timer
def selam(limit, message=None, *args, **kwargs):
    for i in range(0, limit):
        pass
    print(f'selam() {message} finished. {kwargs.get("year")}')
    print(f"args: {args} | kwargs: {kwargs}")


if __name__ == '__main__':
    title = 'python debugging dersi'
    
    
    # breakpoint() # python3.7 +
    
    import pdb; pdb.set_trace()



    result = foo(34)
    print(f"foo() result: {result}")

    info = long_dict()
    print(f"info: {info}")

    d = {str(val): i for i, val in enumerate(compute(3))}
    print(f"computed d: {d}")

    selam(100_000, 'Türkiye', year=2021)
    
    person = Person('adnan', 'https://adnankayace.blogspot.com')
    selam(10_000, person=person, year=2023)
