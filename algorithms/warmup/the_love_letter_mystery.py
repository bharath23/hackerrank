def minPalindrome(s):
    l = 0
    r = len(s) - 1
    n = 0
    while (l < r):
        n += abs(ord(s[l]) - ord(s[r]))
        l = l + 1
        r = r - 1

    return n

n = int(input())
for i in range(0,n):
    a = input()
    res = minPalindrome(a)
    print(res)
