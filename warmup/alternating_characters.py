def numDeletions(a):
    c = a[0]
    b = 0
    for i in a[1:]:
        if i == c:
            b = b + 1
        else:
            c = i
    return b

n = int(input())
for i in range(0,n):
    a = input()
    res = numDeletions(a)
    print(res)
