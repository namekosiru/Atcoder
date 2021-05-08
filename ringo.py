N = int(input())
A = list(map(int, input().split()))

dict_list = {i: 0 for i in range(200)}
ans = 0
for a in A:
    if a < 200:
        num = dict_list[a]
        dict_list[a] = num + 1
    else:
        a = a % 200
        num  = dict_list[a]
        dict_list[a] = num + 1

for i in dict_list.values():
    if i != 0:
        ans += i * (i - 1) //2
print(ans)