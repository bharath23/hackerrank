def genStones(n, a, b):
    if (a == b):
        return [(n - 1) * a]
    stones = set([(n - i - 1) * a + i * b for i in range(n)])
    return sorted(stones)

t = int(input())
for _ in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    a, b = sorted([a,b])
    stones = genStones(n, a, b)
    print(*stones)
