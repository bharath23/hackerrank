n, m = [int(inp) for inp in input().split(" ")]
total = 0
for _ in range(m):
    a, b, k = [int(inp) for inp in input().split(" ")]
    total += (b - a + 1) * k
print(total // n)
