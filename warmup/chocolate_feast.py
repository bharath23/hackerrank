T = int(input())

for i in range(T):
    N,C,M = str(input()).split()
    answer = 0
    # Compute Answer
    w = int(N) // int(C)
    answer += w
    while (w >= int(M)):
        answer +=1
        w -= int(M) - 1
    print(answer)
