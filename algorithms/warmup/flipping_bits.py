def flipBits(a):
    mask = int(0xffffffff)
    return a^mask

n = int(input())
for i in range(0,n):
    a = int(input())
    res = flipBits(a)
    print (res)
