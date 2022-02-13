n = int(input())
s = input()

ans: int = 0
x: int = 0

def max_judge(x: int):
    global ans
    if x > ans:
        ans = x

for si in s:
    if si == "I":
        x += 1
        max_judge(x)
    else:
        x -= 1
        max_judge(x)
print(ans)