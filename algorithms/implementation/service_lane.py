n, t = [int(i) for i in input().split(" ")]
w = [int(i) for i in input().split(" ")]
for _ in range(t):
    i, j = [int(i) for i in input().split(" ")]
    a = 3
    for l in range(i, j + 1):
        if w[l] < a:
            a = w[l]
    print(a)
