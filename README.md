# HSA24
Operation Tree Profiling

This examples display use of profiling to measure time and memory usage for use of Self-Balanced Binary Search Tree
implemented in [Data Structures and Algorithms](https://github.com/mitchsvik/HSA20) repository

### Time profiling

The Python standard library provides `cPython` profiler implemented on C

To run a test with time profiler call:

`python test_bst.py <amount_of_iteration>`

Example of execution for inserts:

```
100000 items profile:
         12467996 function calls (10914871 primitive calls) in 2.209 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.027    0.027    2.209    2.209 ~/HSA/HSA24/test_bst.py:16(test_data_set)
   100000    0.020    0.000    2.062    0.000 ~/HSA/HSA24/bst.py:16(insert)
1653125/100000    1.135    0.000    2.043    0.000 ~/HSA/HSA24/bst.py:20(insert_to_node)
  1553125    0.381    0.000    0.531    0.000 ~/HSA/HSA24/bst.py:141(get_balance)
  6478304    0.324    0.000    0.324    0.000 ~/HSA/HSA24/bst.py:134(get_height)
  1686027    0.140    0.000    0.140    0.000 {built-in method builtins.max}
   100000    0.020    0.000    0.119    0.000 /opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/random.py:358(randint)
   100000    0.048    0.000    0.099    0.000 /opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/random.py:284(randrange)
   100000    0.027    0.000    0.039    0.000 /opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/random.py:235(_randbelow_with_getrandbits)
    34398    0.025    0.000    0.038    0.000 ~/HSA/HSA24/bst.py:170(left_rotate)
    32124    0.024    0.000    0.035    0.000 ~/HSA/HSA24/bst.py:148(right_rotate)
   100000    0.014    0.000    0.014    0.000 ~/HSA/HSA24/bst.py:5(__init__)
   300000    0.012    0.000    0.012    0.000 {built-in method _operator.index}
   130890    0.007    0.000    0.007    0.000 {method 'getrandbits' of '_random.Random' objects}
   100000    0.004    0.000    0.004    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 ~/HSA/HSA24/bst.py:13(__init__)
```

### Search profiling

Example of execution for search:

```
Search 10000 iterations for 500000 items:
         277867 function calls (100465 primitive calls) in 0.049 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10000    0.001    0.000    0.039    0.000 ~/HSA/HSA24/bst.py:54(find)
187402/10000    0.038    0.000    0.038    0.000 ~/HSA/HSA24/bst.py:58(find_in_node)
    10000    0.002    0.000    0.010    0.000 /opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/random.py:358(randint)
    10000    0.004    0.000    0.008    0.000 /opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/random.py:284(randrange)
    10000    0.002    0.000    0.003    0.000 /opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/random.py:235(_randbelow_with_getrandbits)
    30000    0.001    0.000    0.001    0.000 {built-in method _operator.index}
    10464    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
    10000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```


### Memory profiling

As `cProfile` focused on profiling execution timings, for memory profiling can be used `memory-profiler` library

To run a test with memory profiler call:

`mprof run test_bst.py <amount_of_iteration> 1`

Example of execution:

```
mprof: Sampling memory every 0.1s
running new process
running as a Python program...
Filename: test_bst.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     22.0 MiB     22.0 MiB           1   def test_data_set(num_of_items=10000):
    17     22.0 MiB      0.0 MiB           1       iterations = num_of_items
    18     22.0 MiB      0.0 MiB           1       max_value = num_of_items * RANDOM_MULTIPLIER
    19                                         
    20     22.0 MiB      0.0 MiB           1       btree = BalancedTree()
    21     28.9 MiB      0.0 MiB       50001       for _ in range(iterations):
    22     28.9 MiB      1.5 MiB       50000           val = randint(0, max_value)
    23     28.9 MiB      5.4 MiB       50000           btree.insert(val)
    24                                         
    25     28.9 MiB      0.0 MiB           1       return iterations
```


## Results

Iterations | Total Duration | Insert to node | Insert to utilities | Function calls | Memory MiB | Search timing
-----------|----------------|----------------|---------------------|----------------|------------|---------------
50000 | 1,027 | 0,53 | 0,5160662123 | 5862978 | 6,9 | 0,037
100000 | 2,209 | 1,135 | 0,5138071526 | 12467996 | 13,8 | 0,038
150000 | 3,441 | 1,769 | 0,5140947399 | 19329030 | 21,6 | 0,040
200000 | 4,7 | 2,441 | 0,5193617021 | 26295554 | 28,0 | 0,041
250000 | 5,975 | 3,123 | 0,5226778243 | 33344017 | 34,5 | 0,043
500000 | 13,007 | 6,97 | 0,5358653033 | 70265002 | 68,8 | 0,049

### Results

The space complexity is linear O(n).
Insertion complexity with balancing after each iteration also shows linear correlation O(n). It is applicable for BST in the worst case.
Search complexity didn't grow linearly with the change in the amount of items to search and provide O(log(n)) time complexity.
