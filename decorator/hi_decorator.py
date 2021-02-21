'''
To improve, expand the functionality of a method(function),
we use decorators.
'''
import time
import random


def machine_learner(dataset):
    rand = random.randint(1, 5)
    print(f"Learning for dataset: {dataset}")
    print(f"Random number: {rand}")
    time.sleep(rand)


def timer(func):
    def f(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"Elapsed duration: {after-before}")

    return f


get_duration = timer(machine_learner)

get_duration(15)
get_duration(7)