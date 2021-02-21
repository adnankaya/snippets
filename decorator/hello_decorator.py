import time
import random





def timer(func):
    def f(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"Elapsed duration: {after-before}")

    return f

@timer
def machine_learner(dataset):
    rand = random.randint(1, 5)
    print(f"Learning for dataset: {dataset}")
    print(f"Random number: {rand}")
    time.sleep(rand)

machine_learner(15)
machine_learner(7)