from math import sqrt

def isPerfectSqrt(n):
    s = int(sqrt(n))
    if s * s == n:
        return True
    else:
        return False

def isFibo(x):
    a = 5 * x * x + 4
    b = 5 * x * x - 4
    if isPerfectSqrt(a) or isPerfectSqrt(b):
        return 'IsFibo'
    else:
        return 'IsNotFibo'

t = int(input())
for _ in range(t):
    n = int(input())
    res = isFibo(n)
    print(res)
