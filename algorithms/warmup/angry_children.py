import sys

def minUnfairness(a, n, k):
    min_u = sys.maxsize
    a.sort()
    for i in range(n - k + 1):
        u = a[i + k - 1] - a[i]
        if (u < min_u):
            min_u = u

    return min_u

n = int(input())
k = int(input())
a = [int(input()) for i in range(n)]
res = minUnfairness(a, n, k)
print(res)
