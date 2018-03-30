# -*- coding = utf-8 -*-

"""
问题描述
活动序列a(i)，长度为n，共享一个资源，同时有且只有一个活动可以占有该资源，且活动开始必须持续到结束
s(i)和f(i)分别是a(i)的开始和结束时间，f(i)已按从小到大排列
求一个最优方案，从活动a中选出子序列，使可以开展的活动数最大
"""

"""
动态规划
令L(i)是以a(i)结束的最长兼容子序列
那么L(i)=max L(j)+1, 当s(i) >= f(j), j从0...i-1
            L(j), 当s(i) < f(j), j从0...i-1
"""
def dynamic_activity_selector(s, f, n):
    l = [1]*n
    largest = 1
    for i in range(1, n):
        for j in range(0, i):
            cur = l[j]
            if s[i] >= f[j]:
                cur = l[j] + 1
            l[i] = max(l[i], cur)
        if largest < l[i]:
            largest = l[i]
    #print(l)
    return largest

"""
贪婪算法
每次选取活动时，选结束最早的那个
"""
def recursive_activity_selector(s, f, n):
    # 需要加上a[0]，因为recursive_activity_selector_util找的是a[0]结束后最长的活动个数
    return recursive_activity_selector_util(s, f, 0, n)+1

# 寻找第k+1到n中，a[k]结束后能进行的最多的活动个数
# 使用贪婪算法， 每次从剩下的活动中寻找最先结束的活动
def recursive_activity_selector_util(s, f, k, n):
    if k >= n-1:
        return 0
    i = k+1
    while i <= n-1 and s[i] < f[k]:
        i += 1
    return recursive_activity_selector_util(s, f, i, n)+1

def iterative_activity_selector(s, f, n):
    k = 0
    max_activity = 1
    i = 1
    while i < n:
        if s[i] >= f[k]:
            k = i
            max_activity += 1
        i += 1
    return max_activity








