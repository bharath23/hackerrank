def treeHeight(a, b):
    for i in range(0, b):
        if i % 2 == 0:
            a = 2 * a
        else:
            a = a + 1

    return a

n = int(input())
for i in range(0,n):
    a = int(input())
    res = treeHeight(1, a)
    print (res)
