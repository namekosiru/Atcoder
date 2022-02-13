n = int(input())
h = list(map(int, input().split()))
check: list = [False for _ in range(n)]
ans: int = 0
for i in range(len(h)-1):
    if check[i]: continue
    count: int = 0
    for j in range(i, len(h)-1):
        check[j] = True
        if h[j] < h[j+1]:
            break
        count += 1
    ans = max(ans, count)
print(ans)