import random
import timeit
from insertion_method import insertion_sort
from merge_methods import merge_sort


def get_random_array(amount=100000):
    test_array = [random.randint(1, 100) for _ in range(amount)]
    return test_array


def time_tracking(array):
    result = timeit.timeit()
