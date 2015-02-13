n = int(input())
a = [int(i) for i in input().split(" ")]
a.sort()
start = 0
while (start < n):
    cuts = 0
    len = a[start]
    for i in range(start, n):
        if a[i] != 0:
            a[i] -= len
            cuts += 1
            if a[i] == 0:
                start = i + 1
    if cuts == 0:
        break
    print(cuts)
