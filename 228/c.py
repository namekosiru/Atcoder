n, K = map(int, input().split())
sums = []
for i in range(n):
    p1, p2, p3 = map(int, input().split())
    sums.append([i, p1 + p2 + p3])
count = 0
sums = sorted(sums, key=lambda x: x[1], reverse=True)
ans = {}
for k, v in sums:
    if K >= count:
        count += 1
        ans[k] = "Yes"
    else:
        if sums[K-1][1] - v > 300:
            ans[k] = "No"
        else:
            ans[k] = "Yes"

ans = sorted(ans.items(), key=lambda x: x[0])

for i, k in ans:
    print(k)