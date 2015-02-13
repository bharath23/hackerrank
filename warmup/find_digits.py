t = int(input())
for _ in range(t):
    n = int(input())
    d = 10
    c = 0
    n_copy = n
    while (n):
        digit = n % 10
        n = n // 10
        if digit != 0:
            if n_copy % digit == 0:
                c += 1
    print(c)
