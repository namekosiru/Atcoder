N = int(input())

AB = [list(map(int, input().split())) for _ in range(N)]
t = 0
for a, b in AB:
    t += a / b
t *= 0.5
ans = 0
for i in range(N):
    a, b = AB[i]
    ans += min(a, b*t)
    t -= min(a/b, t)

print(ans)