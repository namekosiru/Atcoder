N = int(input())
s = list(input())
q = int(input())
lis = []
for _ in range(q):
    lis.append(list(map(int, input().split())))

for li in lis:
    if li[0] == 1:
        tmp = s[li[1]-1]
        s[li[1]-1] = s[li[2]-1]
        s[li[2]-1] = tmp
    elif li[0] == 2:
        s = s[len(s)//2:] + s[:len(s)//2]
print("".join(s))