h, w = map(int, input().split())

ans: list = [[0] for _ in range(h)]

for i in range(h):
    ans[i] = list(input())

ans.insert(0, ["#"] * (w+2))
ans.append(["#"] * (w+2))
for i in range(1,h+1):
    ans[i].insert(0, "#")
    ans[i].append("#")

for value in ans:
    print("".join(value))