import math
r, x, y = map(int, input().split())

d = math.sqrt(x**2+y**2)

if d < r:
    ans = 2
else:
    ans = -(-d // r)
print(int(ans))