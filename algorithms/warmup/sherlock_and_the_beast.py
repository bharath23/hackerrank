t = int(input())
for _ in range(t):
    n = int(input())
    num = ''
    for i in range(n, -1, -1):
        if (i % 3 == 0) and ((n - i) % 5 == 0):
            num = '5' * i + '3' * (n - i)
            break
    if not num:
        print('-1')
    else:
        print(num)
