n, q = map(int, input().split())
a = list(map(int, input().split()))
dic = {}
for i in range(len(a)):
    if a[i] in dic.keys():
        dic[a[i]].append(i+1)
    else:
        dic[a[i]] = [i+1]
xk = []
for _ in range(q):
    xk.append(list(map(int, input().split())))

for x, k in xk:
    if x not in dic.keys():
        print(-1)
        continue
    if len(dic[x]) < k:
        print(-1)
        continue
    else:
        print(dic[x][k-1])
    