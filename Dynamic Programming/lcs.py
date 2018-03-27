# -*- coding = utf-8 -*-

def lcs_length_brute_force(x, y):
    if not isinstance(x, list) or not isinstance(y, list):
        raise "input is not list"
    m = len(x)
    n = len(y)
    c = [[0 for i in range(n+1)] for j in range(m+1)]
    lcs_length_brute_force_util(x, y, c, m, n)
    print(c)
    print('lcs length: ', c[m][n])

def lcs_length_brute_force_util(x, y, c, ci, cj):
    if ci == 0 or cj == 0:
        c[ci][cj] = 0
        return 0
    if x[ci-1] == y[cj-1]:
        c[ci][cj] = lcs_length_brute_force_util(x, y, c, ci-1, cj-1) + 1
    else:
        c[ci][cj] = max(lcs_length_brute_force_util(x, y, c, ci-1, cj), 
                        lcs_length_brute_force_util(x, y, c, ci, cj-1))
    return c[ci][cj]

# 省空间的蛮力解法
def lcs_length_top_down_optimize(x, y, m, n):
    if m < 0 or n < 0:
        return ""
    if x[m] == y[n]:
        return lcs_length_bottom_up_optimize(x, y, m-1, n-1)+x[m]
    else:
        return maxi(lcs_length_bottom_up_optimize(x, y, m, n-1),
                    lcs_length_bottom_up_optimize(x, y, m-1, n))

def lcs_length_bottom_up(x, y):
    if not isinstance(x, list) or not isinstance(y, list):
        raise "input is not list"
    m = len(x)
    n = len(y)
    c = [[0 for i in range(n+1)] for j in range(m+1)]
    b = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y [j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 'upleft'
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
                if c[i-1][j] > c[i][j-1]:
                    b[i][j] = 'up'
                    c[i][j] = c[i-1][j] 
                else:
                    b[i][j] = 'left'
                    c[i][j] = c[i][j-1] 
    print(c)
    lcs = []
    lcs_print(b, x, m, n, lcs)
    print('lcs length: ', c[m][n])
    print('lcs: ', lcs)

# if we only want the length of LCS, c can be a one dimensional list
def lcs_length_bottom_up_optimize(x, y):
    if not isinstance(x, list) or not isinstance(y, list):
        raise "input is not list"
    m = len(x)
    n = len(y)
    # 空间复杂度O(2*n)
    c = [[0 for j in range(n+1)] for i in range(2)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[1][j] = c[0][j-1] + 1
            else:
                c[1][j] = max(c[0][j], c[1][j-1])
        c[0][:] = c[1][:]
    print('lcs length: ', c[0][n])

def maxi(a, b):
    if len(a) >= len(b):
        return a
    else:
        return b

def lcs_print(b, x, i, j, lcs):
    if i == 0 or j==0:
        return
    if b[i][j] == 'upleft':
        lcs_print(b, x, i-1, j-1, lcs)
        if i > 0:
            lcs.append(x[i-1])
    elif b[i][j] == 'up':
        lcs_print(b, x, i-1, j, lcs)
    else:
        lcs_print(b, x, i, j-1, lcs)


def lcs_length_top_down(x, y):
    if not isinstance(x, list) or not isinstance(y, list):
        raise "input is not list"
    m = len(x)
    n = len(y)
    c = [[0 for i in range(n+1)] for j in range(m+1)]
    lcs_length_top_down_util(x, y, c, m, n)
    print(c)
    print('lcs length: ', c[m][n])

def lcs_length_top_down_util(x, y, c, ci, cj):
    if ci == 0 or cj == 0:
        c[ci][cj] = 0
        return 0
    if c[ci][cj] > 0:
        return c[ci][cj]
    if x[ci-1] == y[cj-1]:
        c[ci][cj] = lcs_length_brute_force_util(x, y, c, ci-1, cj-1) + 1
    else:
        c[ci][cj] = max(lcs_length_brute_force_util(x, y, c, ci-1, cj), 
                        lcs_length_brute_force_util(x, y, c, ci, cj-1))
    return c[ci][cj]


if __name__ == "__main__":
    x = list('ACTB')
    y = list('ATC')
    lcs_length_brute_force(x, y)
    lcs_length_top_down(x, y)
    lcs_length_bottom_up(x, y)
    lcs_length_bottom_up_optimize(x, y)
    lcs = lcs_length_bottom_up_optimize(x, y, len(x)-1, len(y)-1)
    print(lcs)

