w = input()
ans: dict = {}

for wi in w:
    if wi not in ans:
        ans[wi] = 1
    else:
        ans[wi] += 1

for value in ans.values():
    if value % 2 != 0:
        print("No")
        exit()

print("Yes")