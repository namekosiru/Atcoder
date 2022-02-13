s = list(input())

count: int = 0
count_rev: int = 0

tile: dict = {"0": "1", "1":"0"}

if len(s) == 1:
    print(0)
    exit()

for i in range(len(s)-1):
    if (num := s[i+1]) == s[i]:
        s[i+1] = tile[num]
        count += 1

for j in range(len(s), 0, -1):
    if (num := s[i+1]) == s[i]:
        s[i+1] = tile[num]
        count_rev += 1

print(max(count_rev, count))