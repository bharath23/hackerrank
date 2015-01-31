def lonelyinteger(a):
    answer = 0
    for n in a:
        answer ^= n

    return answer

if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
