n = int(input())
a = [[0]*n for _ in range(n)]
b = [[0]*n for _ in range(n)]
for i in range(n):
    s = int(input())
    for j in range(n, 0, -1):
        a[i][j - 1] = s % 10
        s = s // 10
for i in range(n):
    b[0][i] = a[0][i]
    b[n - 1][i] = a[n - 1][i]
    b[i][0] = a[i][0]
    b[i][n - 1] = a[i][n - 1]
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if ((a[i][j] > a[i - 1][j]) and
            (a[i][j] > a[i][j - 1]) and
            (a[i][j] > a[i][j + 1]) and
            (a[i][j] > a[i + 1][j])):
            b[i][j] = 'X'
        else:
            b[i][j] = a[i][j]
for i in range(n):
    print(*b[i], sep='')
