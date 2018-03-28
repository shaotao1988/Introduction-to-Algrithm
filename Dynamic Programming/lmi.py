# -*- coding = utf-8 -*-

# Solution for longest monotonically increasing subsequence of a sequence of n numbers
def lmi(x):
    l = [1 for _ in range(len(x))]
    s = [-1 for _ in range(len(x))]
    largest_index = 0
    for i, xi in enumerate(x[1:], 1):
        for j, xj in enumerate(x[0:i]):
            if xj <= xi:
                #l[i] = max(l[i], l[j]+1)
                if l[i] < l[j]+1:
                    l[i] = l[j]+1
                    s[i] = j
        if l[largest_index] < l[i]:
            largest_index = i
    sq = []
    print_lmi(x, s, sq, largest_index)
    print(x)
    print(l)
    return sq

def print_lmi(x, s, sq, i):
    """
    Input:
        x: input number list
        s: s output by lmi
        i: current index in recurrence
    Output:
        sq: longest monotonically increasing subsequence
    """
    if i == -1:
        return
    print_lmi(x, s, sq, s[i])
    sq.append(x[i])


if __name__ == '__main__':
    x = [1,2,6,4,3,8,6,5,7,3,4,2,1,9,7,8]
    print(lmi(x))