n, m, c = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
for _ in range(n):
    a = list(map(int, input().split()))
    tmp = c
    for ai, bi in zip(a, b):
        tmp += ai*bi
    if tmp > 0:
        ans += 1
print(ans)