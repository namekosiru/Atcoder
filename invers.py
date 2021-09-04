N = int(input())
lis = list(map(int, input().split()))
dic = {}
for i in range(len(lis)):
    dic[i+1] = lis[i]

ans = sorted(dic.items(), key=lambda x:x[1])

for i in ans:
    print(i[0], end=" ")