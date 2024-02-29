import cProfile
import pstats
import io
import sys

from memory_profiler import profile
from pstats import SortKey
from random import randint

from bst import BalancedTree


RANDOM_MULTIPLIER = 1


def test_data_set(num_of_items=10000):
    iterations = num_of_items
    max_value = num_of_items * RANDOM_MULTIPLIER

    btree = BalancedTree()
    for _ in range(iterations):
        val = randint(0, max_value)
        btree.insert(val)

    return iterations, btree


def with_profile(num_of_items):
    # https://docs.python.org/3/library/profile.html#module-cProfile
    pr = cProfile.Profile()
    pr.enable()
    # Profiling test data set
    iterations, _ = test_data_set(num_of_items)
    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    return iterations, s.getvalue()


def check_search_with_profile(btree, num_of_items=1000, num_of_checks=10000):
    max_value = num_of_items * RANDOM_MULTIPLIER
    pr = cProfile.Profile()
    pr.enable()
    for _ in range(num_of_checks):
        val = randint(0, max_value)
        btree.find(val)

    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    return s.getvalue()


def run_iteration(num_of_items=10000, profile_option=0):
    num_of_items = int(num_of_items)
    profile_option = int(profile_option)
    if profile_option == 0:
        iterations, func_profile = with_profile(num_of_items)
        print(f'{iterations} items profile:')
        print(func_profile)
    elif profile_option == 1:
        profile(test_data_set)(num_of_items)
    elif profile_option == 2:
        iterations, btree = test_data_set(num_of_items)
        func_profile = check_search_with_profile(btree, num_of_items)
        print(f'Search 10000 iterations for {iterations} items:')
        print(func_profile)


if __name__ == '__main__':
    args = sys.argv[1:]
    run_iteration(*args)
