from math import sqrt

t = int(input())
for _ in range(t):
    a, b = [int(i) for i in input().split(" ")]
    count = 0
    i = 1;
    s = 1;
    while (s <= b):
        if (s >= a):
            count +=1
        
        i += 1
        s = pow(i, 2)
    print(count)
