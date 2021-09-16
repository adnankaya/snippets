import time

DIGITS = 4


def timer(func):
    def wrapper(*args, **kwargs):
        started = time.time()
        func(*args, **kwargs)
        elapsed = round((time.time() - started), DIGITS)
        print(f"Elapsed {func.__name__}() : {elapsed} seconds.")
    return wrapper


def compute(limit):
    for i in range(limit):
        yield i
    print("finish compute()")


def foo(i) -> float:
    return i*i


def long_dict():
    return {
        'firstname': 'Adnan',
        'lastname': 'Kaya',
        'youtube': 'kayace',
        'github': 'www.github.com/adnankaya',
        'blog': 'www.adnankayace.blogspot.com',
        'programming_languages': [
            'python',
            'javascript',
            'java'
        ]
    }
