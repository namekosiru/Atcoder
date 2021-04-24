N = int(input())
lis = []
for _ in range(2):
    lis.append(list(map(int, input().split())))

lists = []

for a, b in zip(lis[0], lis[1]):
    set_list = []
    for i in range(a, b+1):
        set_list.append(i)
    lists.append(list(set_list))

x = set(lists[0])
for i in range(len(lists)) :
    x = x & set(lists[i])
print(len(x))