from collections import Counter

s = input()
char_count = Counter(s).values()
odds = [ count for count in char_count if count % 2 != 0]
print('YES' if len(odds) <= 1 else 'NO')
