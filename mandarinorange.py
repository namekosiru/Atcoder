N = int(input())

a = list(map(int, input().split()))
ans = 0
for i in range(N):
    orange = a[i]
    for j in range(i, N):
        orange = min(orange, a[j])
        ans = max(ans, orange * (j - i + 1))
print(ans)