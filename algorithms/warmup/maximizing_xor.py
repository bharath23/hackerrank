def maxXor(l, r):
    max = 0
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            xor = i ^ j
            if xor > max:
                max = xor
    return max

if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))

