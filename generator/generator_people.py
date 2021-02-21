import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print ('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))

def xrange(x):
    return iter(range(x))

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in xrange(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

t1 = time.perf_counter()
people = people_list(1_000_000)
t2 = time.perf_counter()

print('people_list Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print('people_list Took {} Seconds'.format(t2-t1))


t1 = time.perf_counter()
people = people_generator(1_000_000)
t2 = time.perf_counter()

print('people_generator Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print('people_generator Took {} Seconds'.format(t2-t1))
