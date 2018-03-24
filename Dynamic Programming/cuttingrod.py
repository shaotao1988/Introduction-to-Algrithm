# -*- coding: utf-8 -*-

# brute force
def cutting_rod_bruteforce(p, n):
    """
    p: price for different length, non negative
    n: length of rod
    return: maximum revenue for n
    """
    if n == 0:
        return 0
    max_r = 0
    for i in range(1, n+1):
        max_r = max(max_r, p[i]+cutting_rod_bruteforce(p, n-i))
    return max_r

# bottom up
def cutting_rod_bottomup(p, n):
    r = [0]*(n+1)
    for i in range(1, n+1):
        max_r = 0
        for j in range(1, i+1):
            max_r = max(p[j] + r[i-j], max_r)
        r[i] = max_r
    return r[n]

# top down
def cutting_rod_topdown(p, n):
    """
    p: price for different length, non negative
    n: length of rod
    return: maximum revenue for n
    """
    # Save the max revenue, 0 for default
    r = [0]*(n+1)
    cutting_rod_topdown_util(p, n, r)
    return r[n]


def cutting_rod_topdown_util(p, n, r):
    if n == 0:
        return 0
    if r[n] != 0:
        return r[n]
    max_r = 0
    for i in range(1, n+1):
        max_r = max(max_r, p[i]+cutting_rod_topdown_util(p, n-i, r))
    r[n] = max_r
    return max_r