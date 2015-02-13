def gcd(a,b):
    b, a = sorted((a,b))
    if b == 0:
        return a
    
    while a:
        a, b = b, a % b
        if b == 0:
            return a
        
def solve(n, a):
    gc = 0
    for i in a:
        gc = gcd(gc, i)
        if gc == 1:
            return 'YES'
    return 'NO'

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split(" ")]
    res = solve(n, a)
    print(res)
