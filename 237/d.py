from collections import deque

n = int(input())
s = input()

a = deque([n])

for i in range(n-1, -1, -1):
    if s[i] == "R":
        a.appendleft(i)
    else:
        a.append(i)

print(*a)
