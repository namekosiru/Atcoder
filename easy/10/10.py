n = int(input())
k = int(input())
x_list = list(map(int, input().split()))
ans = 0
for x in x_list:
    ans += min(x, abs(k-x))*2
print(ans)