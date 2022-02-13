s = input()
cnt = 0
ans = 0
for si in s:
    if si in ["A", "C", "G", "T"]:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
        
print(ans)