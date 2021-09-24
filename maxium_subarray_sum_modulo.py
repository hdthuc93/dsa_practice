#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
    # Write your code here
    max_sum = 0
    cache = [0]*len(a)
    for i in range(len(a)):
        a[i] %= m

    for lvl in range(len(a)):
        print(lvl)
        max_sum = max(max_sum, findMaxSum(a, m, lvl, max_sum, cache))

    return max_sum

def findMaxSum(a, m, lvl, max_sum, cache):
    i = 0
    while i+lvl < len(a):
        sum_cached = cache[i]
        cache[i] = (sum_cached + a[i+lvl])%m
        max_sum = max(max_sum, cache[i])
        i += 1
    return max_sum

if __name__ == '__main__':
    test_case_file = '/Volumes/DATA/Workspace/python/coding_challenge/testcases/maxium_subarray_sum_modulo_test16.txt'
    import time

    with open(test_case_file, 'r') as f:
        q = int(f.readline().strip())
        print(q)

        for q_itr in range(q):
            first_multiple_input = f.readline().rstrip().split()
            n = int(first_multiple_input[0])
            m = int(first_multiple_input[1])
            a = list(map(int, f.readline().rstrip().split()))
            print('Running test', q_itr)
            s = time.time()
            result = maximumSum(a, m)
            print(result, time.time()-s)
