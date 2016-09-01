from __future__ import division, print_function
from random import randint


def has_duplicates(bdays):
    return len(bdays) != len(set(bdays))


def get_random_day():
    return randint(1, 365)


def get_random_day_list(n):
    bdays = []
    for _ in range(n):
        bdays.append(get_random_day())
    return bdays


def get_stat(n_st, n_times):
    count = 0
    for _ in range(n_times):
        if has_duplicates(get_random_day_list(n_st)):
            count += 1
    return count


num_students = 23
num_times = 100
print('number of students: %d' % num_students)
print('number of times: %d' % num_times)
p = get_stat(num_students, num_times)/num_times * 100
print('probability: %d%%' % p)
