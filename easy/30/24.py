a, b, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_min = min(a_list)
b_min = min(b_list)

ans = a_min + b_min

for _ in range(m):
    x, y, c = map(int, input().split())
    if ans >= a_list[x-1] + b_list[y-1] - c:
        ans =  a_list[x-1] + b_list[y-1] - c

print(ans)