N, K = map(int, input().split())
a_list = list(map(int, input().split()))
a_list_sort = sorted(a_list)
output = K // len(a_list)
amari = K % len(a_list)
amari_list = a_list_sort[:amari]
count = len(amari_list)
ans = [output] * len(a_list)
for i in amari_list:
    index = a_list.index(i)
    ans[index] = ans[index] + 1

for i in ans:
    print(i)
