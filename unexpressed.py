import math

N = int(input())

s = set()

for a in range(2, int(math.sqrt(N))+1):
    tmp = a * a
    while tmp <= N:
        s.add(tmp)
        tmp *= a

print(N - len(s))