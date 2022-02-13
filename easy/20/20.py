s = int(input())

a = [s]
count = 0
while count <= 2:
    if s % 2 == 0:
        s = s // 2
    else:
        s = 3*s + 1
    if s == 4:
        count += 1
    a.append(s)

for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            print(j+1)
            exit()
