n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    if i == n-1:
        if x - a[n-1] == 0:
            ans += 1
    elif x - a[i] >= 0:
        x -= a[i]
        ans += 1
    else:
        break

print(ans)
