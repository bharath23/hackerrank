from collections import defaultdict

def one():
    return 1

n, m = [int(i) for i in input().split(" ")]
a = [int(i) for i in input().split(" ")]
b = [int(i) for i in input().split(" ")]
c = [int(i) for i in input().split(" ")]
facts = defaultdict(one)
for i in range(m):
    facts[b[i]] = facts[b[i]] * c[i] % 1000000007

for i, f in facts.items():
    for j in range(i - 1, n, i):
        a[j] = a[j] * f % 1000000007
    
print(*a)
