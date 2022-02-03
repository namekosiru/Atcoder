N = int(input())
x = list(map(int, input().split()))

ans = 10 ** 10
max_num = max(x)
for i in range(1, max_num+1):
    tmp = 0
    for xi in x:
        tmp += (i-xi)**2

    if ans > tmp:
        ans = tmp
print(ans)